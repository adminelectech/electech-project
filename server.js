const express = require('express');
const bcrypt = require('bcryptjs');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const DB_FILE = path.join(__dirname, 'db.json');

// ─── ADMIN PROVISIONING ──────────────────────────────────
async function setupDefaultAdmin() {
    const db = readDB();
    const adminEmail = 'admin@electech.ma';
    
    if (!db.users.find(u => u.email === adminEmail)) {
        const hashedPassword = await bcrypt.hash('ELEC2026', 10);
        const adminUser = {
            id: 999,
            name: 'Administrateur Global',
            email: adminEmail,
            password: hashedPassword,
            role: 'admin',
            profile: {
                city: 'Rabat',
                specialty: 'Expert Ingénierie Électrique',
                experience: '15',
                cvName: 'admin_master_cv.pdf'
            },
            profileComplete: true
        };
        db.users.push(adminUser);
        writeDB(db);
        console.log('✅ Compte Admin provisionné : admin@electech.ma / ELEC2026');
    }
}
setupDefaultAdmin();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname))); // Serve static frontend files

// DB Helper
function readDB() {
    if (!fs.existsSync(DB_FILE)) return { users: [] };
    return JSON.parse(fs.readFileSync(DB_FILE, 'utf8'));
}

function writeDB(data) {
    fs.writeFileSync(DB_FILE, JSON.stringify(data, null, 2));
}

// ─── AUTH APIS ───────────────────────────────────────────

// Register
app.post('/api/register', async (req, res) => {
    const { name, email, password, role } = req.body;
    const db = readDB();
    
    if (db.users.find(u => u.email === email)) {
        return res.status(400).json({ message: 'Cet email est déjà utilisé.' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
        id: Date.now(),
        name,
        email,
        password: hashedPassword,
        role,
        profile: {
            city: '',
            specialty: '',
            experience: '',
            cvName: ''
        },
        profileComplete: false
    };

    db.users.push(newUser);
    writeDB(db);

    res.status(201).json({ 
        message: 'Compte créé avec succès',
        user: { name, email, role, profileComplete: false }
    });
});

// Login
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    const db = readDB();
    const user = db.users.find(u => u.email === email);

    if (!user || !(await bcrypt.compare(password, user.password))) {
        return res.status(401).json({ message: 'Email ou mot de passe incorrect.' });
    }

    res.json({
        message: 'Connexion réussie',
        user: { 
            name: user.name, 
            email: user.email, 
            role: user.role, 
            profileComplete: user.profileComplete 
        }
    });
});

// ─── PROFILE APIS ────────────────────────────────────────

// Get Profile
app.get('/api/profile', (req, res) => {
    const email = req.query.email;
    const db = readDB();
    const user = db.users.find(u => u.email === email);
    
    if (!user) return res.status(404).json({ message: 'Utilisateur non trouvé' });
    res.json(user.profile);
});

// Update Profile
app.post('/api/profile', (req, res) => {
    const { email, profile } = req.body;
    const db = readDB();
    const userIndex = db.users.findIndex(u => u.email === email);

    if (userIndex === -1) return res.status(404).json({ message: 'Utilisateur non trouvé' });

    // Validate completeness
    const isComplete = profile.city && profile.specialty && profile.experience && profile.cvName;
    
    db.users[userIndex].profile = profile;
    db.users[userIndex].profileComplete = !!isComplete;
    
    writeDB(db);

    res.json({ 
        message: 'Profil mis à jour', 
        profileComplete: !!isComplete 
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

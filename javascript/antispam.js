/**
 * ╔══════════════════════════════════════════════════════╗
 * ║        ELECTECH — Puzzle CAPTCHA Anti-Spam          ║
 * ║  Widget glisser-déposer : compléter le circuit ⚡    ║
 * ╚══════════════════════════════════════════════════════╝
 *
 * Usage :
 *   const cap = new PuzzleCaptcha('mon-container-id');
 *   if (!cap.isValid()) { alert("Résolvez le puzzle !"); return; }
 */

class PuzzleCaptcha {
  constructor(containerId, options = {}) {
    this.containerId = containerId;
    this.solved = false;
    this.tolerance = options.tolerance || 12; // pixels d'écart acceptés
    this.onSolve = options.onSolve || null;
    this.render();
  }

  isValid() {
    return this.solved;
  }

  reset() {
    this.solved = false;
    const container = document.getElementById(this.containerId);
    if (container) {
      container.innerHTML = '';
      this.render();
    }
  }

  render() {
    const container = document.getElementById(this.containerId);
    if (!container) return;

    // ── Styles inline du widget ──────────────────────────────────
    container.innerHTML = `
      <div class="antispam-widget">
        <div class="asp-label">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          Vérification Anti-Spam — Glissez la pièce pour compléter le circuit
        </div>
        <div class="asp-track-wrap">
          <!-- Circuit image de fond -->
          <div class="asp-track">
            <div class="asp-circuit-left"></div>
            <div class="asp-gap-zone">
              <div class="asp-gap-target" id="${this.containerId}-target">
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
                  <circle cx="14" cy="14" r="12" fill="rgba(255,140,0,0.08)" stroke="rgba(255,140,0,0.35)" stroke-width="1.5" stroke-dasharray="3 3"/>
                </svg>
              </div>
            </div>
            <div class="asp-circuit-right"></div>
          </div>
          <!-- Pièce glissable -->
          <div class="asp-piece" id="${this.containerId}-piece" title="Glissez vers le circuit →">
            <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
              <!-- Icône éclair = pièce du circuit -->
              <circle cx="14" cy="14" r="13" fill="#FF8C00" stroke="#b35f00" stroke-width="1"/>
              <path d="M15 4 L8 15 L13 15 L11 24 L20 13 L15 13 Z" fill="#000" stroke="none"/>
            </svg>
          </div>
        </div>
        <!-- Status bar -->
        <div class="asp-status" id="${this.containerId}-status">
          <span class="asp-status-idle">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            Faites glisser le ⚡ vers le marqueur orange
          </span>
        </div>
      </div>
    `;

    this._injectStyles();
    this._initDrag();
  }

  _initDrag() {
    const piece = document.getElementById(`${this.containerId}-piece`);
    const target = document.getElementById(`${this.containerId}-target`);
    const status = document.getElementById(`${this.containerId}-status`);
    if (!piece || !target) return;

    let dragging = false;
    let startX = 0;
    let pieceStartX = 0;

    const getX = (e) => e.touches ? e.touches[0].clientX : e.clientX;

    const trackWrap = piece.parentElement;
    const trackRect = () => trackWrap.getBoundingClientRect();

    const onStart = (e) => {
      if (this.solved) return;
      dragging = true;
      startX = getX(e);
      pieceStartX = piece.offsetLeft;
      piece.style.cursor = 'grabbing';
      piece.style.transition = 'none';
      e.preventDefault();
    };

    const onMove = (e) => {
      if (!dragging) return;
      const dx = getX(e) - startX;
      const rect = trackRect();
      const maxRight = rect.width - piece.offsetWidth - 4;
      let newLeft = Math.min(Math.max(0, pieceStartX + dx), maxRight);
      piece.style.left = newLeft + 'px';
      e.preventDefault();
    };

    const onEnd = () => {
      if (!dragging) return;
      dragging = false;
      piece.style.cursor = 'grab';

      const pieceRect = piece.getBoundingClientRect();
      const targetRect = target.getBoundingClientRect();

      const pCenterX = pieceRect.left + pieceRect.width / 2;
      const tCenterX = targetRect.left + targetRect.width / 2;
      const pCenterY = pieceRect.top + pieceRect.height / 2;
      const tCenterY = targetRect.top + targetRect.height / 2;

      const dist = Math.sqrt((pCenterX - tCenterX) ** 2 + (pCenterY - tCenterY) ** 2);

      if (dist <= this.tolerance + 15) {
        // ✅ Succès : snapper la pièce
        piece.style.transition = 'left 0.2s ease, box-shadow 0.3s';
        const snap = targetRect.left - piece.parentElement.getBoundingClientRect().left + (targetRect.width - piece.offsetWidth) / 2;
        piece.style.left = snap + 'px';
        this._setSolved(piece, status);
      } else {
        // ❌ Retour à la position initiale
        piece.style.transition = 'left 0.4s cubic-bezier(.68,-0.55,.27,1.55)';
        piece.style.left = '4px';
        status.innerHTML = `<span class="asp-status-error">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
          Réessayez, guidez le ⚡ jusqu'au cercle pointillé
        </span>`;
      }
    };

    // Mouse
    piece.addEventListener('mousedown', onStart);
    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onEnd);

    // Touch
    piece.addEventListener('touchstart', onStart, { passive: false });
    document.addEventListener('touchmove', onMove, { passive: false });
    document.addEventListener('touchend', onEnd);
  }

  _setSolved(piece, status) {
    this.solved = true;
    piece.style.background = 'linear-gradient(135deg,#1a3a1a,#0d2a0d)';
    piece.style.border = '1.5px solid #22c55e';
    piece.style.boxShadow = '0 0 12px rgba(34,197,94,0.4)';
    piece.querySelector('svg circle').setAttribute('fill', '#22c55e');
    piece.style.cursor = 'default';

    status.innerHTML = `<span class="asp-status-ok">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
      Circuit validé — Vous êtes humain ✓
    </span>`;

    if (typeof this.onSolve === 'function') this.onSolve();
  }

  _injectStyles() {
    if (document.getElementById('antispam-styles')) return;
    const style = document.createElement('style');
    style.id = 'antispam-styles';
    style.textContent = `
      .antispam-widget {
        background: #0a0a0a;
        border: 1px solid #1f2937;
        border-radius: 0.85rem;
        padding: 1rem 1.2rem;
        user-select: none;
        -webkit-user-select: none;
      }
      .asp-label {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #6b7280;
        margin-bottom: 0.85rem;
      }
      .asp-label svg { color: #FF8C00; flex-shrink: 0; }

      /* Track */
      .asp-track-wrap {
        position: relative;
        height: 52px;
        background: #111;
        border: 1px solid #1f2937;
        border-radius: 0.65rem;
        overflow: hidden;
        display: flex;
        align-items: center;
      }
      .asp-track {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        pointer-events: none;
      }
      /* Circuit lines */
      .asp-circuit-left, .asp-circuit-right {
        height: 3px;
        flex: 1;
        background: repeating-linear-gradient(
          90deg,
          #FF8C00 0, #FF8C00 8px,
          transparent 8px, transparent 14px
        );
        opacity: 0.25;
      }
      .asp-circuit-left { margin-left: 48px; }
      .asp-circuit-right { margin-right: 16px; }
      .asp-gap-zone {
        width: 60px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 1;
      }
      .asp-gap-target {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
      }

      /* Sliding piece */
      .asp-piece {
        position: absolute;
        left: 4px;
        top: 50%;
        transform: translateY(-50%);
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1a1a1a, #111);
        border: 1.5px solid #FF8C00;
        box-shadow: 0 0 10px rgba(255,140,0,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: grab;
        z-index: 10;
        transition: box-shadow 0.3s;
      }
      .asp-piece:hover {
        box-shadow: 0 0 16px rgba(255,140,0,0.5);
      }

      /* Status bar */
      .asp-status {
        margin-top: 0.6rem;
        font-size: 10px;
        font-weight: 700;
      }
      .asp-status-idle { display: flex; align-items: center; gap: 5px; color: #4b5563; }
      .asp-status-ok   { display: flex; align-items: center; gap: 5px; color: #22c55e; }
      .asp-status-error { display: flex; align-items: center; gap: 5px; color: #ef4444; }
    `;
    document.head.appendChild(style);
  }
}

/* ── Helper global ───────────────────────────────────────────────────
   Bloque la soumission si le captcha n'est pas résolu.
   Ajoute un message d'erreur temporaire sous le bouton.
──────────────────────────────────────────────────────────────────── */
function checkPuzzle(captchaInstance, submitBtn) {
  if (!captchaInstance.isValid()) {
    // Message d'erreur
    let errEl = document.getElementById('asp-submit-error');
    if (!errEl) {
      errEl = document.createElement('p');
      errEl.id = 'asp-submit-error';
      errEl.style.cssText = 'color:#ef4444;font-size:11px;font-weight:700;margin-top:8px;display:flex;align-items:center;gap:5px;';
      if (submitBtn && submitBtn.parentNode) submitBtn.parentNode.insertBefore(errEl, submitBtn.nextSibling);
    }
    errEl.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 9v4M12 17h.01M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/></svg> Résolvez le puzzle anti-spam avant de continuer.';
    errEl.style.display = 'flex';
    setTimeout(() => { if (errEl) errEl.style.display = 'none'; }, 4000);
    // Shake l'élément captcha
    const w = document.querySelector('.antispam-widget');
    if (w) {
      w.style.animation = 'aspShake 0.4s ease';
      setTimeout(() => w.style.animation = '', 400);
    }
    return false;
  }
  return true;
}

// Shake animation globale
(function () {
  const s = document.createElement('style');
  s.textContent = `@keyframes aspShake {
    0%,100%{transform:translateX(0)}
    20%{transform:translateX(-5px)}
    40%{transform:translateX(5px)}
    60%{transform:translateX(-4px)}
    80%{transform:translateX(4px)}
  }`;
  document.head.appendChild(s);
})();

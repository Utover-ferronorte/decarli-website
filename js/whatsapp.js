/* ─────────────────────────────────────────
   DE CARLI – Floating WhatsApp Button
   Glassmorphism / Liquid Glass style
   ───────────────────────────────────────── */

(function () {
  const css = `
    #wa-float {
      position: fixed;
      bottom: 32px;
      right: 32px;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 14px;
      font-family: 'Montserrat', Arial, sans-serif;
    }

    /* ── Painel expandido ── */
    #wa-panel {
      opacity: 0;
      transform: translateY(20px) scale(0.92);
      pointer-events: none;
      transition: opacity 0.38s ease, transform 0.38s cubic-bezier(0.34,1.56,0.64,1);
      transform-origin: bottom right;
    }
    #wa-panel.open {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: all;
    }

    /* ── Caixa de glass ── */
    #wa-box {
      background: rgba(20, 20, 30, 0.55);
      backdrop-filter: blur(28px) saturate(180%);
      -webkit-backdrop-filter: blur(28px) saturate(180%);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 20px;
      padding: 18px 18px 14px;
      min-width: 248px;
      box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        0 1px 0 rgba(255,255,255,0.12) inset;
    }

    #wa-box-title {
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.9);
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(255,255,255,0.12);
    }

    /* ── Links WhatsApp ── */
    .wa-link {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      border-radius: 12px;
      background: rgba(37,211,102,0.9);
      border: 1px solid rgba(255,255,255,0.25);
      color: #fff;
      text-decoration: none;
      font-size: 0.7rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      transition: background 0.22s ease, transform 0.22s ease, box-shadow 0.22s ease;
      box-shadow: 0 4px 14px rgba(37,211,102,0.3);
      margin-bottom: 8px;
    }
    .wa-link:last-child { margin-bottom: 0; }
    .wa-link:hover {
      background: rgba(37,211,102,1);
      transform: translateX(-3px);
      box-shadow: 0 6px 20px rgba(37,211,102,0.5);
    }
    .wa-link svg { flex-shrink: 0; }
    .wa-link-text { display: flex; flex-direction: column; gap: 1px; }
    .wa-link-label { font-size: 0.55rem; opacity: 0.75; font-weight: 400; letter-spacing: 0.1em; }
    .wa-link-unit  { font-size: 0.75rem; font-weight: 700; letter-spacing: 0.04em; }

    /* ── Wrapper do botão + pulse ── */
    #wa-btn-wrap {
      position: relative;
      width: 58px;
      height: 58px;
      flex-shrink: 0;
    }

    /* anéis removidos */
    .wa-ring { display: none; }

    /* ── Botão principal ── */
    #wa-toggle {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      border: 1.5px solid rgba(255,255,255,0.35);
      background: rgba(14, 39, 65, 0.9);
      backdrop-filter: blur(16px) saturate(200%);
      -webkit-backdrop-filter: blur(16px) saturate(200%);
      box-shadow:
        0 8px 28px rgba(14,39,65,0.5),
        0 2px 6px rgba(0,0,0,0.2),
        0 1px 0 rgba(255,255,255,0.2) inset;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition:
        transform 0.35s cubic-bezier(0.34,1.56,0.64,1),
        box-shadow 0.3s ease,
        background 0.3s ease;
      overflow: hidden;
    }

    /* Glare */
    #wa-toggle::before {
      content: '';
      position: absolute;
      top: -20%;
      left: -5%;
      width: 110%;
      height: 55%;
      background: linear-gradient(180deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 100%);
      border-radius: 50%;
      pointer-events: none;
      transition: opacity 0.3s;
    }

    #wa-toggle:hover {
      transform: scale(1.12);
      box-shadow: 0 14px 40px rgba(14,39,65,0.6), 0 2px 8px rgba(0,0,0,0.2);
    }

    #wa-btn-wrap.active #wa-toggle {
      background: rgba(255,255,255,0.2);
      box-shadow: 0 8px 24px rgba(0,0,0,0.2), 0 1px 0 rgba(255,255,255,0.4) inset;
    }
    #wa-btn-wrap.active #wa-toggle::before { opacity: 0.5; }

    /* ── Ícones dentro do botão ── */
    #wa-toggle .icon-wa,
    #wa-toggle .icon-cls {
      position: absolute;
      transition: opacity 0.25s ease, transform 0.3s cubic-bezier(0.34,1.56,0.64,1);
    }
    #wa-toggle .icon-wa  { opacity: 1; transform: scale(1) rotate(0deg); }
    #wa-toggle .icon-cls { opacity: 0; transform: scale(0.5) rotate(-90deg); }

    #wa-btn-wrap.active #wa-toggle .icon-wa  { opacity: 0; transform: scale(0.5) rotate(90deg); }
    #wa-btn-wrap.active #wa-toggle .icon-cls { opacity: 1; transform: scale(1) rotate(0deg); }

    @media (max-width: 480px) {
      #wa-float { bottom: 20px; right: 18px; }
      #wa-box { min-width: 220px; }
    }
  `;

  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  const waIcon = `<svg class="icon-wa" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
    <line x1="9" y1="10" x2="15" y2="10"/>
    <line x1="9" y1="14" x2="13" y2="14"/>
  </svg>`;

  const closeIcon = `<svg class="icon-cls" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
  </svg>`;

  const waLinkSVG = `<svg width="22" height="22" viewBox="0 0 24 24" fill="white">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
  </svg>`;

  const html = `
    <!-- Painel -->
    <div id="wa-panel">
      <div id="wa-box">
        <div id="wa-box-title">Fale conosco pelo WhatsApp</div>
        <a class="wa-link"
          href="https://api.whatsapp.com/send/?phone=%2B555433117505&text&type=phone_number&app_absent=0"
          target="_blank" rel="noopener">
          ${waLinkSVG}
          <div class="wa-link-text">
            <span class="wa-link-label">WhatsApp</span>
            <span class="wa-link-unit">Und. Passo Fundo</span>
          </div>
        </a>
        <a class="wa-link"
          href="https://api.whatsapp.com/send/?phone=%2B5551998067391&text&type=phone_number&app_absent=0"
          target="_blank" rel="noopener">
          ${waLinkSVG}
          <div class="wa-link-text">
            <span class="wa-link-label">WhatsApp</span>
            <span class="wa-link-unit">Und. Porto Alegre</span>
          </div>
        </a>
      </div>
    </div>

    <!-- Botão + anéis -->
    <div id="wa-btn-wrap">
      <div class="wa-ring"></div>
      <div class="wa-ring"></div>
      <div class="wa-ring"></div>
      <button id="wa-toggle" aria-label="Abrir WhatsApp">
        ${waIcon}
        ${closeIcon}
      </button>
    </div>
  `;

  const wrapper = document.createElement('div');
  wrapper.id = 'wa-float';
  wrapper.innerHTML = html;
  document.body.appendChild(wrapper);

  const toggle  = document.getElementById('wa-toggle');
  const btnWrap = document.getElementById('wa-btn-wrap');
  const panel   = document.getElementById('wa-panel');

  toggle.addEventListener('click', () => {
    const isOpen = panel.classList.contains('open');
    panel.classList.toggle('open', !isOpen);
    btnWrap.classList.toggle('active', !isOpen);
  });

  document.addEventListener('click', (e) => {
    if (!wrapper.contains(e.target)) {
      panel.classList.remove('open');
      btnWrap.classList.remove('active');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      panel.classList.remove('open');
      btnWrap.classList.remove('active');
    }
  });
})();

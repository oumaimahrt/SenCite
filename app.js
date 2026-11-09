// ==========================================================================
// SenCité - Plateforme du Quotient Émotionnel (Prototype Interactif)
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
    // 1. Tab Switching
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');

            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            btn.classList.add('active');
            const targetContent = document.getElementById(targetTab);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });

    // 2. Real-time Sliders & Live Calculation
    const sliders = {
        lumiere: document.getElementById('slider-lumiere'),
        son: document.getElementById('slider-son'),
        securite: document.getElementById('slider-securite'),
        social: document.getElementById('slider-social'),
        attachement: document.getElementById('slider-attachement'),
        nature: document.getElementById('slider-nature')
    };

    const valDisplays = {
        lumiere: document.getElementById('val-lumiere'),
        son: document.getElementById('val-son'),
        securite: document.getElementById('val-securite'),
        social: document.getElementById('val-social'),
        attachement: document.getElementById('val-attachement'),
        nature: document.getElementById('val-nature')
    };

    // Update individual values on slide
    Object.keys(sliders).forEach(key => {
        if (sliders[key] && valDisplays[key]) {
            sliders[key].addEventListener('input', (e) => {
                valDisplays[key].textContent = `${e.target.value}%`;
                updateLiveScore();
            });
        }
    });

    function updateLiveScore() {
        const l = parseInt(sliders.lumiere.value, 10);
        const s = parseInt(sliders.son.value, 10);
        const sec = parseInt(sliders.securite.value, 10);
        const soc = parseInt(sliders.social.value, 10);
        const a = parseInt(sliders.attachement.value, 10);
        const n = parseInt(sliders.nature.value, 10);

        // Formule de Quotient Émotionnel pondérée (Méthodologie SenCité)
        // Piliers sensoriels (40%) + Piliers psychologiques & sociaux (60%)
        const globalScore = Math.round(
            (l * 0.18) + (s * 0.15) + (sec * 0.22) + (soc * 0.18) + (a * 0.15) + (n * 0.12)
        );

        // Update Big Score
        const scoreNumEl = document.getElementById('global-qe-score');
        const modalScoreEl = document.getElementById('modal-score');
        const scoreStatusEl = document.getElementById('score-status');

        if (scoreNumEl) scoreNumEl.textContent = globalScore;
        if (modalScoreEl) modalScoreEl.textContent = `${globalScore}/100`;

        // Update Qualitative Status
        if (scoreStatusEl) {
            if (globalScore >= 80) {
                scoreStatusEl.textContent = "Espace d'Exception • Rayonnement Sensible Remarquable";
                scoreStatusEl.style.color = "var(--accent-forest)";
            } else if (globalScore >= 65) {
                scoreStatusEl.textContent = "Espace Qualitatif & Harmonieux (Frictions ciblées)";
                scoreStatusEl.style.color = "var(--text-primary)";
            } else if (globalScore >= 50) {
                scoreStatusEl.textContent = "Espace Contrasté • Irritants Sensibles Identifiés";
                scoreStatusEl.style.color = "var(--accent-gold)";
            } else {
                scoreStatusEl.textContent = "Espace Vulnérable • Action Programmatique Urgente";
                scoreStatusEl.style.color = "var(--accent-terracotta)";
            }
        }

        // Update Dimension Bars in Tab 2
        updateBar('lumiere', l);
        updateBar('son', s);
        updateBar('securite', sec);
        updateBar('social', soc);
        updateBar('attachement', a);
        updateBar('nature', n);
    }

    function updateBar(key, val) {
        const textEl = document.getElementById(`bar-val-${key}`);
        const fillEl = document.getElementById(`bar-fill-${key}`);
        if (textEl) textEl.textContent = `${val}/100`;
        if (fillEl) fillEl.style.width = `${val}%`;
    }

    // Sync button navigates to Tab 2
    const btnSync = document.getElementById('btn-sync-score');
    if (btnSync) {
        btnSync.addEventListener('click', () => {
            updateLiveScore();
            const scoringTabBtn = document.querySelector('[data-tab="tab-scoring"]');
            if (scoringTabBtn) scoringTabBtn.click();
        });
    }

    // 3. AI NLP Playground & Verbatims
    const presets = {
        1: {
            text: "En journée l'allée centrale est très agréable et vivante, mais dès que la nuit tombe vers 19h, l'éclairage trop tamisé crée des zones d'ombre anxiogènes vers les arrêts de tramway.",
            badges: [
                { text: "Convivialité diurne (+0.81)", type: "positive" },
                { text: "Insécurité nocturne (-0.89)", type: "negative" },
                { text: "Éclairage déficitaire : Tramway", type: "warning" }
            ],
            rec: "« Le sentiment de vulnérabilité est corrélé au gradient lumineux après 19h. Recommandation : implanter un éclairage dynamique rasant et chaleureux sur le cheminement piéton menant au tramway. »"
        },
        2: {
            text: "C'est un véritable tiers-lieu vivant ! On croise aussi bien des architectes que des voisins qui viennent prendre un café sous la verrière. Il y a une ambiance bienveillante très rare dans le quartier.",
            badges: [
                { text: "Sentiment de communauté (+0.95)", type: "positive" },
                { text: "Altérité & Mixité d'usage (+0.90)", type: "positive" },
                { text: "Attachement fort au lieu (+0.88)", type: "positive" }
            ],
            rec: "« Signature relationnelle exceptionnelle. Le lieu incarne parfaitement « ce qui nous relie ». Préconisation : sanctuariser les espaces de transition informelle et favoriser la programmation participative. »"
        },
        3: {
            text: "C'est beaucoup trop minéral, en été c'est une fournaise et on entend le bourdonnement continuel des climatiseurs et des camions. On a envie de fuir vers un parc pour respirer.",
            badges: [
                { text: "Stress thermique (-0.92)", type: "negative" },
                { text: "Pollution sonore continue (-0.79)", type: "negative" },
                { text: "Rejet de l'espace / Évitement", type: "warning" }
            ],
            rec: "« Rupture sensible majeure. Recommandation programmatique prioritaire : désimperméabilisation des sols, création d'un îlot de fraîcheur arboré et isolation acoustique des groupes froids. »"
        }
    };

    const verbatimInput = document.getElementById('user-verbatim');
    const presetBtns = document.querySelectorAll('.preset-btn');
    const btnRunAi = document.getElementById('btn-run-ai');
    const aiSpinner = document.getElementById('ai-spinner');
    const aiContent = document.getElementById('ai-content');

    let currentPreset = 1;

    presetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.getAttribute('data-preset');
            if (presets[id]) {
                currentPreset = id;
                verbatimInput.value = presets[id].text;
            }
        });
    });

    if (btnRunAi) {
        btnRunAi.addEventListener('click', () => {
            aiSpinner.style.display = 'flex';
            aiContent.style.opacity = '0.2';

            setTimeout(() => {
                aiSpinner.style.display = 'none';
                aiContent.style.opacity = '1';

                const data = presets[currentPreset] || presets[1];
                
                // Render badges
                const tagsContainer = aiContent.querySelector('.emotion-tags');
                if (tagsContainer) {
                    tagsContainer.innerHTML = data.badges.map(b => 
                        `<span class="badge badge-${b.type}">${b.text}</span>`
                    ).join('');
                }

                // Render Recommendation
                const quoteEl = aiContent.querySelector('.ai-quote');
                if (quoteEl) quoteEl.textContent = data.rec;
            }, 750);
        });
    }

    // 4. Modal Client Report
    const btnExport = document.getElementById('btn-export-preview');
    const modal = document.getElementById('report-modal');
    const btnClose1 = document.getElementById('btn-close-modal');
    const btnClose2 = document.getElementById('btn-close-modal-2');

    if (btnExport && modal) {
        btnExport.addEventListener('click', () => {
            modal.classList.add('active');
        });
    }

    [btnClose1, btnClose2].forEach(btn => {
        if (btn && modal) {
            btn.addEventListener('click', () => {
                modal.classList.remove('active');
            });
        }
    });

    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('active');
        });
    }

    // Initial calculation on load
    updateLiveScore();
});

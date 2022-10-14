"use strict";

// language popup
(function() {
    const langBtn = document.querySelector('.languages__current_lang');
    const languagesGroup = document.querySelector('.languages-group');
    langBtn.addEventListener('click', () => {
        languagesGroup.classList.toggle('active');
    });
})();

// send form
(function() {
    const homeForm = document.querySelector("#contact-form");
    if (homeForm) {
        homeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const fields = e.target.querySelectorAll('input, textarea');
            const contactData = new FormData();
            const submitBtn = homeForm.querySelector('[type="submit"]');
            submitBtn.setAttribute('disabled', true);
            submitBtn.innerText = submitBtn.getAttribute('data-loading');
            for (const field of fields) {
                contactData.append(field.getAttribute('name'), field.value);
            }
            const formAction = homeForm.getAttribute('action');
            try {
                const result = await fetch(formAction, {
                    method: 'POST',
                    body: contactData
                }).then(res => {
                    if (res.ok) {
                        return res.json();
                    } else {
                        throw {'error': 'Bad request'};
                    }
                });
                submitBtn.innerText = submitBtn.getAttribute('data-success');
            } catch(e) {
                submitBtn.innerText = submitBtn.getAttribute('data-error');
                console.warn(e);
            }
        });
    }

})();
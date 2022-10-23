"use strict";

// language popup
(function() {
    const languageForm = $('.language-form');
    const languageSelect = $('[name="language"]');
    languageSelect.on('change', () => languageForm.submit());
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

// news slider
(function() {
    $('.news-slider').slick({
        'draggable': false,
    });
    const popup = $('.news-popup');
    $('.news-slide, .news-item__btn').on('click', async function(e) {
        const postUrl = $(this).attr('data-url');
        const payload = new FormData();
        payload.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        try {
            const post = await fetch(postUrl, {
                method: 'POST',
                body: payload
            }).then(res => {
                if (res.ok) {
                    return res.text();
                }
                throw {'status': 'bad request'};
            });
            popup.find('.news-popup-inner').html(post);
            initLikes();
            popup.addClass('active');
            $('body').css('overflow', 'hidden');
        } catch(e) {
            console.warn(e);
        }
    });
    $('body').on('click', '.news-single__close', function(e) {
        popup.removeClass('active');
        $('body').css('overflow', '');
    });

    function initLikes() {
        let likes = localStorage.getItem('likes') ? localStorage.getItem('likes') : '';
        likes = likes.split(',');
        const likeBtn = $('.post-header__btn_add-to-favorite');
        if (likes.includes(likeBtn.attr('data-id'))) {
            likeBtn.addClass('checked');
        } else {
            likeBtn.removeClass('checked');
        }
        likeBtn.on('click', async function(e) {
            const likeUrl = likeBtn.hasClass('checked') ? likeBtn.attr('data-delete-like') : likeBtn.attr('data-add-like');
            console.log(likes);
            if (likeBtn.hasClass('checked')) {
                likes = likes.filter((val) => {
                    return val != likeBtn.attr('data-id');
                });
                likeBtn.removeClass('checked');
            } else {
                likes.push(likeBtn.attr('data-id'));
                likeBtn.addClass('checked');
            }
            localStorage.setItem('likes', likes.join(','));
            const payload = new FormData();
            payload.append('csrfmiddlewaretoken', likeBtn.find('[name="csrfmiddlewaretoken"]').val());
            likeBtn.attr('disabled', true);
            try {
                const result = await fetch(likeUrl, {
                    method: 'POST',
                    body: payload
                }).then(res => {
                    if (res.ok) {
                        return res.json();
                    }
                    throw {'500': 'Bad request'}
                });
                likeBtn.find('.cnt').attr('data-likes', result?.likes);
                likeBtn.find('.cnt').text(result?.likes);
                likeBtn.attr('disabled', false);
            } catch(e) {
                console.warn(e);
            }
        });
    }
})();

// sending comments
(function() {
    $('body').on('submit', '.post-comments__form', async function(e) {
        e.preventDefault();
        const btn = $(this).find('[type="submit"]');
        $(this).addClass('loading');
        const commentUrl = $(this).attr('action');
        const payload = new FormData();
        $(this).find('input, textarea').each(function() {
            const inputElement = $(this);
            payload.append(inputElement.attr('name'), inputElement.val());
        });

        try {
            const result = await fetch(commentUrl, {
                method: 'POST',
                body: payload
            }).then(res => {
                if (res.ok) {
                    return res.text();
                }
                throw {'Error': 'Bad request'};
            });

            $(this).find('textarea').val('');
            $(this).removeClass('loading');
            $(this).addClass('done');
            $('.post-comments').prepend(result);
        } catch(e) {
            console.warn(e);
        }
    });
})();

// cases slider
(function() {
    const slider = $('.cases-slider');
    slider.slick({
        infinite: false,
    });
})();
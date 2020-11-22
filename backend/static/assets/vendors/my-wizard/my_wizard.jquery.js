(function ($) {
    $.fn.wizard = function (options) {
        const defaults = {};
        return this.each(function () {
            const $wizard = $(this);
            const $steps = $wizard.children('.steps').find('li');
            const $content = $wizard.children('.content');
            const $actions = $wizard.children('.actions');
            const $next = $actions.find('#action_next');
            const $previous = $actions.find('#action_prev');
            const $finish = $actions.find('#action_finish');

            function getCurrentContent() {
                return $content.children('section').filter('.current');
            }

            function showNextContent() {
                const $currentContent = getCurrentContent();

                const $nextContent = $currentContent.next();
                if ($nextContent.length > 0) {
                    $currentContent.removeClass('current');
                    $nextContent.addClass('current');
                    if ($currentContent.css('pointer-events') !== "none") {

                    } else {

                    }
                    $currentContent.fadeTo('fast', 0);
                    $nextContent.show();
                    $nextContent.fadeTo('normal', 1);

                    // steps
                    $steps.removeClass('disabled');
                    const $current_step = $steps.filter('.current');
                    $current_step.removeClass('current').addClass('disabled');

                    if ($current_step.nextAll().length > 0) {
                        $current_step.next().addClass('current');
                    }
                }

                return $currentContent;
            }

            function showPreviousContent() {
                const $currentContent = getCurrentContent();

                const $previousContent = $currentContent.prev();
                if ($previousContent.length > 0) {
                    $currentContent.removeClass('current');
                    $previousContent.addClass('current');
                    $currentContent.fadeTo('fast', 0, '', function () {
                        $currentContent.hide()
                    });
                    if ($previousContent.css('pointer-events') !== 'none') {
                        $previousContent.fadeTo('normal', 1);
                    } else {
                        $previousContent.fadeTo('fast', 0.5);
                    }

                    $steps.removeClass('disabled');
                    const $current_step = $steps.filter('.current');
                    $current_step.removeClass('current').addClass('disabled');

                    if ($current_step.prevAll().length > 0) {
                        $current_step.prev().addClass('current');
                    }
                }

                return $currentContent
            }

            $next.on('click', function (event) {
                if ($(this).hasClass('disabled')) {
                    return false;
                }
                $previous.parent().show();
                const $currentContent = showNextContent();
                if ($currentContent.nextAll().length === 1) {
                    $finish.parent().show()
                    $next.parent().hide()
                }
                return false;
            });

            $previous.on('click', function (event) {
                if ($(this).hasClass('disabled')) {
                    return false;
                }
                showPreviousContent()
                if (getCurrentContent().prevAll().length === 0) {
                    $previous.parent().hide()
                }
                if ($finish.is(':visible')) {
                    $finish.parent().hide()
                    $next.parent().show()
                }
                return false;
            });

            $finish.on('click', function (event) {
            })

        });
    }
})(jQuery)
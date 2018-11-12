function initList(url, elementId) {
    $.ajax({
        url, success(result) {
            for (let featureRequest of result) {
                $(`#${elementId}`).append(
                    $(`<div class='featureRequest'>${featureRequest['title']}</div>`)
                );
            }
        }
    });
}
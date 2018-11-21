let api = (function () {
    let limit = 10
    let offset = 0
    let count = 0
    let apiUrl;
    let listElementId;

    function handleLongString(s, max_length) {
        return s.length > max_length ? s.substring(0, max_length - 3) + '...' : s
    }

    $('#next').click(() => {
        if (offset + limit < count) {
            offset += limit;
            updateList(apiUrl, listElementId)
        }
    })

    $('#prev').click(() => {
        if (offset - limit >= 0) {
            offset -= limit;
            updateList(apiUrl, listElementId)
        }
    })

    function initList(url, elementId) {
        apiUrl = url
        listElementId = elementId
        updateList(url, elementId)
    }

    function updateList(url, elementId) {
        $.ajax({
            url,
            type: 'get',
            data: {
                limit,
                offset
            },
            success(result) {
                count = result.count
                $(`#${elementId}`).empty()
                for (let featureRequest of result.data) {
                    $('#ajaxTemplate').tmpl(featureRequest).appendTo(`#${elementId}`)
                }
            }
        });
    }

    function displayFlash() {
        $('#flashModal').modal('show')
    }

    return {
        displayFlash,
        initList
    }
})()
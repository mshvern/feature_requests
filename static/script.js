function handleLongString(s, max_length){
    return s.length > max_length? s.substring(0,max_length-3) + '...' : s
}

function getModalId(featureRequest){
    return 'modal' + featureRequest['client'].replace(' ', '') + featureRequest['clientPriority']
}

function initList(url, elementId) {
    $.ajax({
        url, success(result) {
            for (let featureRequest of result) {
                $(`#${elementId}`).append(
                    $(
                    `<div class='row'>
                        <div class='col-sm-4'>
                            ${handleLongString(featureRequest['title'], 30)}
                        </div>
                        <div class='col-sm-2'>
                            ${featureRequest['date']}
                        </div>
                        <div class='col-sm-2'>
                            ${handleLongString(featureRequest['client'], 15)}
                        </div>
                        <div class='col-sm-1'>
                            ${featureRequest['clientPriority']}
                        </div>
                        <div class='col-sm-2'>
                            ${handleLongString(featureRequest['productArea'], 15)}
                        </div>
                        <div class='col-sm-1'>
                            <button type="button" class="btn btn-info" data-toggle="modal" 
                            data-target="#${getModalId(featureRequest)}">info</button>
                        </button>
                        </div>
                    </div>
                    <div class="modal fade" id="${getModalId(featureRequest)}" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">Feature Request Info</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <b>Title: </b> ${featureRequest['title']} </br>
                            <b>Description: </b> ${featureRequest['description']} </br>
                            <b>Client Name: </b> ${featureRequest['client']} </br>
                            <b>Client Priority: </b> ${featureRequest['clientPriority']} </br>
                            <b>Product Area: </b> ${featureRequest['productArea']} </br>
                            <b>Target Date: </b> ${featureRequest['date']}
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                        </div>
                    </div>
                    </div>
                    `
                    )
                );
            }
        }
    });
}
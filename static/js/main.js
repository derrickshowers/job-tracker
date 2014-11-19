$("#newJobForm").submit(function(e){
    console.log(e);
    var isValid = validateForm(this);
    return isValid;
});

function validateForm(form) {
    var isFormValid = false;
    isFormValid = errorMessage(form.title);
    isFormValid = errorMessage(form.company);
    return isFormValid;
}

function errorMessage(field){
    $(field).removeClass("error");
    $(field).next().remove();
    var errorMessageEl = '<small class="error">Invalid entry</small>';
    if(field.value === ""){
        $(field).addClass("error");
        $(field).after(errorMessageEl);
        return false;
    } else {
        return true;
    }
}

$('#newJob').click(function(e){
    $('#newJobForm').find("input").val("");
});
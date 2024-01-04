$(document).ready(function () {
    // Add a click event listener to all "Open Form" buttons
    $('.open-form-btn').on('click', function () {
        // Show the corresponding modal form
        $('#formModal').modal('show');
        
        // Populate the form fields with the values from the clicked row
        var row = $(this).closest('tr');
        $('#edit-semester').val(row.data('semester'));
        $('#edit-exam_type').val(row.data('exam-type'));
        $('#edit-grade').val(row.data('grade'));
        $('#edit-course_code').val(row.data('course-code'));
        $('#edit-lecturer').val(row.data('lecturer'));
        $('#edit-notes').val(row.data('notes'));
        $('#hidden-file-name').val(row.data('file-name'));
    });
});
$(document).ready(function () {
    // Add a click event listener to all "Open Form" buttons
    $('.open-form-btn').on('click', function () {
        // Show the corresponding modal form
        $('#formModal').modal('show');
        
        // Populate the form fields with the values from the clicked row
        var row = $(this).closest('tr');
        $('#edit-semester').val(row.data('semester'));
        $('#edit-exam_type').val(row.data('exam-type'));
        $('#edit-grade').val(row.data('grade'));
        $('#edit-course_code').val(row.data('course-code'));
        $('#edit-lecturer').val(row.data('lecturer'));
        $('#edit-notes').val(row.data('notes'));
        $('#hidden-file-name').val(row.data('file-name'));
    });
});

$(document).ready(function() {
    // Add an event listener to the file input element
    const fileInput = $("#file-upload");
    const fileInputLabel = $(".file-upload-label");

    fileInput.change(function () {
        if (fileInput[0].files.length > 0) {
            // A file has been selected, update the label text
            fileInputLabel.text(`קובץ נבחר`);
        } else {
            // No file selected, revert to the original label text
            fileInputLabel.text("בחר קובץ");
        }
    });
});

$(document).ready(function() {
    $('#datatable').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/he.json'
        },
        fixedColumns: {
            left: 1,
            right: 1
        },
        paging: true,
        scrollCollapse: true,
        scrollX: true,
        bInfo : false
    });
});
// Form validation function
function validateUploadForm() {
    var lecturerInput = document.getElementById("lecturer").value;
    var notesInput = document.getElementById("notes").value;
    var courseCodeInput = document.getElementById("course_code").value;
    var gradeInput = document.getElementById("grade").value;
    var fileInput = document.getElementById("file-upload");
    
    // Regular expressions for validation
    var lecturerRegex = /^$|^[A-Za-z\sא-ת!,'."״]+|\d{1,2}\s?ד"ר\s[A-Za-z\sא-ת!,'."״]+$/;
    var notesRegex = /^$|^[A-Za-z0-9\sא-ת!,'"״\-\/]+$/;
    var numberRegex = /^[0-9]+$/; // Only numbers

    if (!lecturerRegex.test(lecturerInput)) {
        alert("מרצה יכול להכיל רק אותיות, רווחים, אותיות עבריות, !, ,, ., ' ו־״.");
        return false;
    }

    if (!notesRegex.test(notesInput)) {
        alert("הערות יכולות להכיל רק אותיות, מספרים, רווחים, אותיות עבריות, !, ,, ., ' ו־״.");
        return false;
    }

    if (!numberRegex.test(courseCodeInput)) {
        alert("מספר קורס יכול להכיל רק מספרים.");
        return false;
    }

    if (!numberRegex.test(gradeInput)) {
        alert("ציון יכול להכיל רק מספרים.");
        return false;
    }
    if (fileInput.files.length === 0) {
        alert("בחר קובץ לפני העלאה.");
        return false;
    }
    return true;
}
// Form validation function
function validateEditForm() {
    var lecturerInput = document.getElementById("edit-lecturer").value;
    var notesInput = document.getElementById("edit-notes").value;
    var courseCodeInput = document.getElementById("edit-course_code").value;
    var gradeInput = document.getElementById("edit-grade").value;
    
    // Regular expressions for validation
    var lecturerRegex = /^$|^[A-Za-z\sא-ת!,'."״]+|\d{1,2}\s?ד"ר\s[A-Za-z\sא-ת!,'."״]+$/;
    var lecturerRegex = /^$|^[A-Za-z\sא-ת!,'."״]+|\d{1,2}\s?ד"ר\s[A-Za-z\sא-ת!,'."״]+$/;
    var numberRegex = /^[0-9]+$/; // Only numbers

    if (!lecturerRegex.test(lecturerInput)) {
        alert("מרצה יכול להכיל רק אותיות, רווחים, אותיות עבריות, !, ,, ., ' ו־״.");
        return false;
    }

    if (!notesRegex.test(notesInput)) {
        alert("הערות יכולות להכיל רק אותיות, מספרים, רווחים, אותיות עבריות, !, ,, ., ' ו־״.");
        return false;
    }

    if (!numberRegex.test(courseCodeInput)) {
        alert("מספר קורס יכול להכיל רק מספרים.");
        return false;
    }

    if (!numberRegex.test(gradeInput)) {
        alert("ציון יכול להכיל רק מספרים.");
        return false;
    }
    return true;
}




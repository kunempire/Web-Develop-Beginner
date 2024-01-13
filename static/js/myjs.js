/* drag image */
document.addEventListener('DOMContentLoaded', function () {
    var dropArea = document.getElementById('drop-area');

    // prevent default event
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(function (eventName) {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    // style
    ['dragenter', 'dragover'].forEach(function (eventName) {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(function (eventName) {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    // deal with dragging
    dropArea.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight() {
        dropArea.classList.add('bg-light');
    }

    function unhighlight() {
        dropArea.classList.remove('bg-light');
    }

    function handleDrop(e) {
        var dt = e.dataTransfer;
        var files = dt.files;

        handleFiles(files);
    }

    function handleFiles(files) {
        var file = files[0];

        if (file.type.startsWith('image/')) { // limit flie to image
            var reader = new FileReader();

            reader.onload = function (e) {
                dropArea.querySelector('#image-preview').src = e.target.result;
            };

            reader.readAsDataURL(file);
        } else {
            alert('Please select an image!');
        }
    }
});

/* select image */

var dropArea = document.getElementById('drop-area');
var imagePreview = document.getElementById('image-preview');

// monitor click event
dropArea.addEventListener('click', function () {

    var fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'image/*';

    fileInput.addEventListener('change', function () {

        var selectedFile = fileInput.files[0];

        if (selectedFile) {
            // read image
            var reader = new FileReader();
            reader.onload = function (e) {
                imagePreview.src = e.target.result;
            };
            reader.readAsDataURL(selectedFile);
        }
    });

    // simulate click
    fileInput.click();
});
const regex = /^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$/;
const urlInput = document.getElementById('urlInput');
const submitBtn = document.getElementById('submitBtn');
const message = document.getElementById('message');

submitBtn.disabled = true;
message.classList.add('hidden');

urlInput.addEventListener('input', function() {
    const urlValue = urlInput.value.trim();
    if (regex.test(urlValue)) {
        submitBtn.disabled = false;
        message.classList.add('hidden');
    } else {
        submitBtn.disabled = true;
        message.classList.remove('hidden');
    }
});

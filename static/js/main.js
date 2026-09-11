// FreelanceHub - Main JS

// Auto-dismiss alerts after 5s
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(a => {
            let bsAlert = bootstrap.Alert.getOrCreateInstance(a);
            bsAlert.close();
        });
    }, 5000);
});

// Star rating UI
document.querySelectorAll('.star-rating-input').forEach(container => {
    const stars = container.querySelectorAll('label');
    stars.forEach(star => {
        star.addEventListener('mouseover', () => {
            star.style.color = '#ffc107';
        });
    });
});

// Preview profile picture before upload
const picInput = document.getElementById('id_profile_picture');
if (picInput) {
    picInput.addEventListener('change', function () {
        const preview = document.getElementById('pic-preview');
        if (preview && this.files[0]) {
            preview.src = URL.createObjectURL(this.files[0]);
        }
    });
}

// Scroll chat to bottom
const chatBox = document.querySelector('.chat-box');
if (chatBox) {
    chatBox.scrollTop = chatBox.scrollHeight;
}

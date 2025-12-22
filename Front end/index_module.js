// Get elements
const moduleBox = document.getElementById('moduleBox');
const moduleOverlay = document.getElementById('moduleOverlay');
const closeOverlay = document.getElementById('modulecloseOverlay');
const readonlyInput = document.getElementById('moduleoverlayInput');
const textareaInput = document.getElementById('module_overlayInputOverlay');

// Open overlay when clicking the search box
moduleBox.addEventListener('click', function() {
  moduleOverlay.style.display = 'block';
      document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
  textareaInput.focus(); // Focus on textarea
});

// Close overlay when clicking X button
closeOverlay.addEventListener('click', function() {
  moduleOverlay.style.display = 'none';
  document.body.style.overflow = ''; // Unfreeze main screen
  textareaInput.value = ''; // Optional: clear textarea
});

// Optional: Close overlay when pressing Escape key
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape' && moduleOverlay.style.display === 'block') {
    closeOverlay.click();
  }
});






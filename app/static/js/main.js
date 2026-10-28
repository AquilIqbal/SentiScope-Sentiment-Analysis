document.addEventListener('DOMContentLoaded', function () {
  const navbar = document.querySelector('.navbar');
  const fadeItems = document.querySelectorAll('.fade-in');
  const analysisForm = document.getElementById('analysisForm');
  const textArea = document.getElementById('review');
  const charCounter = document.getElementById('charCounter');
  const clearButton = document.getElementById('clearButton');
  const exampleButton = document.getElementById('exampleButton');
  const analyzeButton = document.getElementById('analyzeButton');
  const spinner = analyzeButton ? analyzeButton.querySelector('.spinner-border') : null;
  const buttonLabel = analyzeButton ? analyzeButton.querySelector('.button-label') : null;
  const resultContent = document.getElementById('resultContent');
  const resultCard = document.getElementById('resultCard');

  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 10);
    });
  }

  if (fadeItems.length > 0) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.2
    });

    fadeItems.forEach(function (item) {
      observer.observe(item);
    });
  }

  function updateCharCounter() {
    if (charCounter && textArea) {
      const count = textArea.value.length;
      charCounter.textContent = count + ' / 500';
      charCounter.classList.toggle('text-danger', count > 500);
    }
  }

  function showEmptyState() {
    if (resultContent) {
      resultContent.innerHTML = `
        <div class="text-center py-4 px-2 analysis-placeholder">
          <div class="icon-box icon-box-sm mx-auto mb-3"><i class="bi bi-clipboard-check"></i></div>
          <h4 class="h6 fw-semibold mb-2">Your analysis will appear here</h4>
          <p class="text-muted mb-0">Submit a review to see the predicted sentiment, confidence score, cleaned text, and a concise interpretation.</p>
        </div>
      `;
    }
  }

  function showWarning(message) {
    if (resultContent) {
      resultContent.innerHTML = `
        <div class="alert alert-warning rounded-4 border-0 shadow-sm" role="alert">
          <div class="d-flex gap-2">
            <i class="bi bi-exclamation-triangle-fill mt-1"></i>
            <div>
              <h4 class="h6 fw-semibold mb-1">Review Needed</h4>
              <p class="mb-0">${message}</p>
            </div>
          </div>
        </div>
      `;
    }
  }

  if (textArea) {
    textArea.addEventListener('input', updateCharCounter);
    updateCharCounter();
  }

  if (clearButton) {
    clearButton.addEventListener('click', function () {
      if (textArea) {
        textArea.value = '';
        updateCharCounter();
        textArea.focus();
      }
      showEmptyState();
      if (resultCard) {
        resultCard.setAttribute('data-success-result', 'false');
      }
    });
  }

  if (exampleButton && textArea) {
    exampleButton.addEventListener('click', function () {
      textArea.value = 'The checkout experience was smooth and the support team resolved my issue quickly. I would definitely recommend this service to others.';
      updateCharCounter();
      textArea.focus();
    });
  }

  if (analysisForm) {
    analysisForm.addEventListener('submit', function (event) {
      const trimmedReview = textArea ? textArea.value.trim() : '';

      if (!trimmedReview) {
        event.preventDefault();
        showWarning('Please enter a review before analyzing it.');
        return;
      }

      if (analyzeButton && analyzeButton.dataset.submitting === 'true') {
        event.preventDefault();
        return;
      }

      if (analyzeButton) {
        analyzeButton.disabled = true;
        analyzeButton.dataset.submitting = 'true';
        if (buttonLabel) {
          buttonLabel.textContent = 'Analyzing...';
        }
        if (spinner) {
          spinner.classList.remove('d-none');
        }
      }
    });
  }

  if (resultCard && resultCard.dataset.successResult === 'true') {
    window.setTimeout(function () {
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 180);
  }

  document.addEventListener('click', function (event) {
    const copyButton = event.target.closest('.copy-cleaned-btn');

    if (!copyButton) {
      return;
    }

    const targetId = copyButton.getAttribute('data-copy-target');
    const targetEl = targetId ? document.getElementById(targetId) : null;

    if (!targetEl) {
      return;
    }

    const copyText = targetEl.textContent;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(copyText).then(function () {
        copyButton.innerHTML = '<i class="bi bi-check2 me-1"></i> Copied';
        window.setTimeout(function () {
          copyButton.innerHTML = '<i class="bi bi-clipboard me-1"></i> Copy';
        }, 1500);
      });
    }
  });
});

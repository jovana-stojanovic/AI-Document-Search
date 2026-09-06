const form = document.querySelector('#question-form');
const questionInput = document.querySelector('#question');
const submitButton = form.querySelector('button');
const status = document.querySelector('#status');
const result = document.querySelector('#result');
const answer = document.querySelector('#answer');
const sources = document.querySelector('#sources');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const question = questionInput.value.trim();

  if (!question) return;

  submitButton.disabled = true;
  status.textContent = 'Searching your documents...';
  status.classList.remove('error');
  result.hidden = true;

  try {
    const response = await fetch('http://127.0.0.1:8000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      throw new Error(`Request failed (${response.status})`);
    }

    const data = await response.json();
    answer.textContent = data.answer ?? 'No answer returned.';
    sources.replaceChildren();

    const sourceItems = Array.isArray(data.sources) ? data.sources : [];
    if (sourceItems.length === 0) {
      const item = document.createElement('li');
      item.textContent = 'No sources returned.';
      sources.append(item);
    } else {
      sourceItems.forEach((source) => {
        const item = document.createElement('li');
        item.textContent = typeof source === 'string' ? source : JSON.stringify(source);
        sources.append(item);
      });
    }

    status.textContent = '';
    result.hidden = false;
  } catch (error) {
    status.textContent = `Unable to get an answer: ${error.message}`;
    status.classList.add('error');
  } finally {
    submitButton.disabled = false;
  }
});

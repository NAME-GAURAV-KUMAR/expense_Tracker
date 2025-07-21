document.addEventListener('DOMContentLoaded', () => {
  const expenseForm = document.getElementById('expense-form');
  const expenseTableBody = document.querySelector('#expense-table tbody');
  const remainingBalanceDisplay = document.getElementById('remaining-balance');

  // Fetch and display expenses
  function loadExpenses() {
      fetch('/api/expenses')
          .then(response => response.json())
          .then(data => {
              expenseTableBody.innerHTML = '';
              data.forEach(expense => {
                  const tr = document.createElement('tr');
                  tr.innerHTML = `
                      <td>${expense.title}</td>
                      <td>$${expense.amount.toFixed(2)}</td>
                      <td>${expense.date}</td>
                      <td><button class="delete-btn" onclick="deleteExpense(${expense.id})">Delete</button></td>
                  `;
                  expenseTableBody.appendChild(tr);
              });
          });
  }

  // Fetch and update the remaining balance
  function updateRemainingBalance() {
      fetch('/api/balance')
          .then(response => response.json())
          .then(data => {
              remainingBalanceDisplay.textContent = `Remaining Balance: $${data.remaining_balance.toFixed(2)}`;
          });
  }

  loadExpenses();
  updateRemainingBalance();

  // Add expense
  expenseForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const title = document.getElementById('title').value;
      const amount = parseFloat(document.getElementById('amount').value);
      const date = document.getElementById('date').value;

      fetch('/api/expenses', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ title, amount, date })
      })
      .then(response => response.json())
      .then(data => {
          expenseForm.reset();
          loadExpenses();
          updateRemainingBalance();
      });
  });
});

// Delete expense
function deleteExpense(id) {
  fetch(`/api/expenses/${id}`, {
      method: 'DELETE'
  })
  .then(response => response.json())
  .then(data => {
      // Reload expenses and update balance
      document.dispatchEvent(new Event('DOMContentLoaded'));
  });
}

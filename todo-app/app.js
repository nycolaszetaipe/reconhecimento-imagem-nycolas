/* ============================================================
   TaskFlow — app.js
   Vanilla JS | localStorage persistence | No dependencies
   ============================================================ */

// ─── DB Helpers ──────────────────────────────────────────────────────────────

function getDB() {
  const raw = localStorage.getItem('taskflow_db');
  if (raw) return JSON.parse(raw);
  const initial = { users: [], todos: [] };
  saveDB(initial);
  return initial;
}

function saveDB(db) {
  localStorage.setItem('taskflow_db', JSON.stringify(db));
}

// ─── Session Helpers ─────────────────────────────────────────────────────────

function getCurrentUser() {
  const raw = localStorage.getItem('currentUser');
  return raw ? JSON.parse(raw) : null;
}

function setCurrentUser(user) {
  localStorage.setItem('currentUser', JSON.stringify(user));
}

function clearCurrentUser() {
  localStorage.removeItem('currentUser');
}

// ─── Screen Router ────────────────────────────────────────────────────────────

const screens = ['login', 'register', 'dashboard'];

function showScreen(name) {
  screens.forEach(id => {
    const el = document.getElementById(`screen-${id}`);
    if (el) {
      el.classList.add('hidden');
    }
  });
  const target = document.getElementById(`screen-${name}`);
  if (target) {
    target.classList.remove('hidden');
  }
}

// ─── Alert Helpers ────────────────────────────────────────────────────────────

function showAlert(elementId, message, type = 'error') {
  const el = document.getElementById(elementId);
  if (!el) return;
  el.textContent = message;
  el.className = el.className.replace(/alert-\w+/g, '');
  el.classList.remove('hidden');
  el.classList.add(type === 'error' ? 'alert-error' : 'alert-success');
  el.classList.add('rounded-lg', 'px-4', 'py-3', 'text-sm');
}

function hideAlert(elementId) {
  const el = document.getElementById(elementId);
  if (el) el.classList.add('hidden');
}

// ─── AUTH: Register ───────────────────────────────────────────────────────────

document.getElementById('register-form').addEventListener('submit', function (e) {
  e.preventDefault();
  hideAlert('register-alert');

  const name     = document.getElementById('register-name').value.trim();
  const email    = document.getElementById('register-email').value.trim().toLowerCase();
  const password = document.getElementById('register-password').value;

  // Validation
  if (!name) {
    showAlert('register-alert', 'Por favor, informe seu nome completo.');
    return;
  }
  if (!email) {
    showAlert('register-alert', 'Por favor, informe um e-mail válido.');
    return;
  }
  if (!password) {
    showAlert('register-alert', 'Por favor, crie uma senha.');
    return;
  }
  if (password.length < 6) {
    showAlert('register-alert', 'A senha deve ter pelo menos 6 caracteres.');
    return;
  }

  const db = getDB();
  const exists = db.users.find(u => u.email === email);
  if (exists) {
    showAlert('register-alert', 'Este e-mail já está cadastrado. Faça login.');
    return;
  }

  // Save user
  const newUser = { name, email, password, createdAt: Date.now() };
  db.users.push(newUser);
  saveDB(db);

  // Auto-login
  setCurrentUser({ name, email });
  showAlert('register-alert', 'Conta criada com sucesso! Redirecionando...', 'success');
  setTimeout(() => initDashboard(), 700);
});

// ─── AUTH: Login ──────────────────────────────────────────────────────────────

document.getElementById('login-form').addEventListener('submit', function (e) {
  e.preventDefault();
  hideAlert('login-alert');

  const email    = document.getElementById('login-email').value.trim().toLowerCase();
  const password = document.getElementById('login-password').value;

  if (!email) {
    showAlert('login-alert', 'Por favor, informe seu e-mail.');
    return;
  }
  if (!password) {
    showAlert('login-alert', 'Por favor, informe sua senha.');
    return;
  }

  const db   = getDB();
  const user = db.users.find(u => u.email === email);

  if (!user) {
    showAlert('login-alert', 'E-mail não encontrado. Verifique ou crie uma conta.');
    return;
  }
  if (user.password !== password) {
    showAlert('login-alert', 'Senha incorreta. Tente novamente.');
    return;
  }

  setCurrentUser({ name: user.name, email: user.email });
  initDashboard();
});

// ─── AUTH: Logout ─────────────────────────────────────────────────────────────

document.getElementById('logout-btn').addEventListener('click', function () {
  clearCurrentUser();
  document.getElementById('login-email').value = '';
  document.getElementById('login-password').value = '';
  hideAlert('login-alert');
  showScreen('login');
});

// ─── Screen Navigation ────────────────────────────────────────────────────────

document.getElementById('go-register').addEventListener('click', function () {
  hideAlert('login-alert');
  hideAlert('register-alert');
  showScreen('register');
});

document.getElementById('go-login').addEventListener('click', function () {
  hideAlert('register-alert');
  hideAlert('login-alert');
  showScreen('login');
});

// ─── Dashboard: Init ─────────────────────────────────────────────────────────

function initDashboard() {
  const user = getCurrentUser();
  if (!user) {
    showScreen('login');
    return;
  }

  // Greet user
  const firstName = user.name.split(' ')[0];
  document.getElementById('header-username').textContent = firstName;

  // Clear form
  document.getElementById('task-form').reset();
  hideAlert('task-alert');

  // Render tasks
  renderTasks();
  showScreen('dashboard');
}

// ─── TASKS: Add ───────────────────────────────────────────────────────────────

document.getElementById('task-form').addEventListener('submit', function (e) {
  e.preventDefault();
  hideAlert('task-alert');

  const title       = document.getElementById('task-title').value.trim();
  const type        = document.getElementById('task-type').value;
  const description = document.getElementById('task-description').value.trim();
  const user        = getCurrentUser();

  if (!title) {
    showAlert('task-alert', 'O título da tarefa é obrigatório.');
    return;
  }

  const newTodo = {
    id:          Date.now(),
    userId:      user.email,
    title,
    type,
    description,
    done:        false,
    createdAt:   Date.now(),
  };

  const db = getDB();
  db.todos.push(newTodo);
  saveDB(db);

  // Reset form fields (keep type select)
  document.getElementById('task-title').value = '';
  document.getElementById('task-description').value = '';

  renderTasks();
});

// ─── TASKS: Toggle Done ───────────────────────────────────────────────────────

function toggleDone(todoId) {
  const db   = getDB();
  const todo = db.todos.find(t => t.id === todoId);
  if (todo) {
    todo.done = !todo.done;
    saveDB(db);
    renderTasks();
  }
}

// ─── TASKS: Delete ────────────────────────────────────────────────────────────

function deleteTask(todoId) {
  const db   = getDB();
  db.todos   = db.todos.filter(t => t.id !== todoId);
  saveDB(db);
  renderTasks();
}

// ─── TASKS: Badge Config ─────────────────────────────────────────────────────

const BADGE_CONFIG = {
  'Trabalho': { css: 'badge-work',     icon: '💼' },
  'Pessoal':  { css: 'badge-personal', icon: '🏠' },
  'Estudos':  { css: 'badge-study',    icon: '📚' },
};

// ─── TASKS: Render ────────────────────────────────────────────────────────────

function renderTasks() {
  const user    = getCurrentUser();
  const db      = getDB();
  const listEl  = document.getElementById('task-list');

  // Filter by current user
  const userTodos = db.todos.filter(t => t.userId === user.email);

  // Sort: pending first, then done
  const pending = userTodos.filter(t => !t.done);
  const done    = userTodos.filter(t => t.done);
  const sorted  = [...pending, ...done];

  // Update stats
  document.getElementById('stat-total').textContent   = userTodos.length;
  document.getElementById('stat-pending').textContent = pending.length;
  document.getElementById('stat-done').textContent    = done.length;

  if (sorted.length === 0) {
    listEl.innerHTML = buildEmptyState();
    return;
  }

  listEl.innerHTML = sorted.map(todo => buildTaskCard(todo)).join('');

  // Attach event listeners
  listEl.querySelectorAll('[data-toggle]').forEach(btn => {
    btn.addEventListener('click', () => toggleDone(Number(btn.dataset.toggle)));
  });

  listEl.querySelectorAll('[data-delete]').forEach(btn => {
    btn.addEventListener('click', () => deleteTask(Number(btn.dataset.delete)));
  });
}

// ─── TASKS: Build Card HTML ──────────────────────────────────────────────────

function buildTaskCard(todo) {
  const badge     = BADGE_CONFIG[todo.type] || BADGE_CONFIG['Trabalho'];
  const doneClass = todo.done ? 'task-done' : '';
  const createdAt = new Date(todo.createdAt).toLocaleDateString('pt-BR', {
    day: '2-digit', month: 'short', year: 'numeric',
  });

  const descriptionHTML = todo.description
    ? `<p class="text-slate-400 text-sm mt-2 leading-relaxed">${escapeHtml(todo.description)}</p>`
    : '';

  const toggleLabel = todo.done ? 'Reabrir' : 'Concluir';
  const toggleIcon  = todo.done
    ? `<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
       </svg>`
    : `<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
       </svg>`;

  return `
    <div class="glass-card-darker rounded-xl p-4 ${doneClass} transition-all duration-300">
      <div class="flex items-start gap-3">

        <!-- Checkbox indicator -->
        <div class="flex-shrink-0 mt-0.5">
          <div class="w-5 h-5 rounded-full border-2 ${todo.done ? 'bg-emerald-500 border-emerald-500' : 'border-slate-600'} flex items-center justify-center transition-all duration-200">
            ${todo.done ? '<svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"/></svg>' : ''}
          </div>
        </div>

        <!-- Content -->
        <div class="flex-1 min-w-0">
          <div class="flex flex-wrap items-center gap-2 mb-1">
            <span class="task-title text-sm font-semibold text-white truncate">${escapeHtml(todo.title)}</span>
            <span class="inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-full ${badge.css}">
              ${badge.icon} ${todo.type}
            </span>
          </div>
          ${descriptionHTML}
          <p class="text-slate-500 text-xs mt-2">${createdAt}</p>
        </div>

        <!-- Actions -->
        <div class="flex-shrink-0 flex items-center gap-1.5">
          <button
            data-toggle="${todo.id}"
            title="${toggleLabel}"
            class="btn-success flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium text-emerald-300"
          >
            ${toggleIcon}
            ${toggleLabel}
          </button>
          <button
            data-delete="${todo.id}"
            title="Excluir tarefa"
            class="btn-danger flex items-center justify-center w-8 h-8 rounded-lg text-red-300"
          >
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
            </svg>
          </button>
        </div>

      </div>
    </div>
  `;
}

// ─── TASKS: Empty State ───────────────────────────────────────────────────────

function buildEmptyState() {
  return `
    <div class="glass-card-darker rounded-2xl p-10 text-center">
      <div class="w-14 h-14 rounded-2xl bg-slate-800 flex items-center justify-center mx-auto mb-4">
        <svg class="w-7 h-7 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
        </svg>
      </div>
      <p class="text-slate-300 font-medium">Nenhuma tarefa cadastrada ainda.</p>
      <p class="text-slate-500 text-sm mt-1">Adicione sua primeira tarefa usando o formulário acima.</p>
    </div>
  `;
}

// ─── Utils ────────────────────────────────────────────────────────────────────

function escapeHtml(str) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
  return String(str).replace(/[&<>"']/g, m => map[m]);
}

// ─── App Init ─────────────────────────────────────────────────────────────────

(function init() {
  const user = getCurrentUser();
  if (user) {
    initDashboard();
  } else {
    showScreen('login');
  }
})();

document.addEventListener('DOMContentLoaded', function () {
  renderTodos();
});

let todos = [];

function addTodo() {
  const newTodoInput = document.getElementById('new-todo');
  const newTodoText = newTodoInput.value.trim();
  if (newTodoText !== '') {
    const todo = { text: newTodoText, done: false };
    todos.push(todo);
    newTodoInput.value = '';
    renderTodos();
  }
}

function toggleTodo(index) {
  todos[index].done = !todos[index].done;
  renderTodos();
}

function deleteTodo(index) {
  todos.splice(index, 1);
  renderTodos();
}

function renderTodos() {
  const todoList = document.getElementById('todo-list');
  todoList.innerHTML = '';
  todos.forEach((todo, index) => {
    const li = document.createElement('li');
    li.className = todo.done ? 'done' : '';
    li.innerHTML = `${todo.text} <button onclick='toggleTodo(${index})'>Toggle</button> <button onclick='deleteTodo(${index})'>Delete</button>`;
    todoList.appendChild(li);
  });
}


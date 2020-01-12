<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Tarefas</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
      <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Tarefa</button>
        <br><br>
        <table class="table table">
          <thead class="thead-dark table-sm">
            <tr>
              <th scope="col">Nome da Tarefa</th>
              <th scope="col">Autor</th>
              <th scope="col">Feita?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
            <tr v-for="(task, index) in tasks" :key="index">
              <td>{{ task.title }}</td>
              <td>{{ task.author }}</td>
              <td>
                <span v-if="task.done">Sim</span>
                <span v-else>Não</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-outline-warning btn-sm"
                    v-b-modal.task-update-modal
                    @click="editTask(task)">
                    Atualizar
                  </button>⠀
                  <button
                    type="button"
                    class="btn btn-outline-danger btn-sm"
                    @click="onDeleteTask(task)">
                    Deletar
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Adicionar uma nova Tarefa"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Nome da tarefa:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addTaskForm.title"
                        required
                        placeholder="">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Autor:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addTaskForm.author"
                          required
                          placeholder="">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-done-group">
          <b-form-checkbox-group v-model="addTaskForm.done" id="form-checks">
            <b-form-checkbox value="true">Feita?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" style="background-color:#42b983;border-color:#42b983"
          class="btn btn-sm" variant="primary">Adicionar tarefa</b-button>⠀
          <b-button type="reset" class="btn btn-sm" variant="danger">Resetar</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editTaskModal"
      id="task-update-modal"
      title="Atualizar"
      hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-title-edit-group"
      label="Nome da Tarefa:"
      label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
        type="text"
        v-model="editForm.title"
        required
        placeholder="">
      </b-form-input>
      </b-form-group>
       <b-form-group id="form-author-edit-group"
         label="Autor:"
         label-for="form-author-edit-input">
         <b-form-input id="form-author-edit-input"
           type="text"
           v-model="editForm.author"
           required
           placeholder="">
         </b-form-input>
       </b-form-group>
       <b-form-group id="form-done-edit-group">
         <b-form-checkbox-group v-model="editForm.done" id="form-checks">
         <b-form-checkbox value="true">Feita?</b-form-checkbox>
         </b-form-checkbox-group>
       </b-form-group>
       <b-button-group>
          <b-button type="submit"
          class="btn btn-warning btn-sm" variant="primary">Atualizar
          </b-button>⠀
          <b-button type="reset" class="btn btn-danger btn-sm" variant="danger">Cancelar</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      tasks: [],
      addTaskForm: {
        title: '',
        author: '',
        done: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        done: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Tarefa adicionada!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.author = '';
      this.addTaskForm.done = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let done = false;
      if (this.addTaskForm.done[0]) done = true;
      const payload = {
        title: this.addTaskForm.title,
        author: this.addTaskForm.author,
        done, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
    editTask(task) {
      this.editForm = task;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      let done = false;
      if (this.editForm.done[0]) done = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        done,
      };
      this.updateTask(payload, this.editForm.id);
    },
    updateTask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Tarefa atualizada!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      this.initForm();
      this.getTasks();
    },
    removeTask(taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.delete(path)
        .then(() => {
          this.getTasks();
          this.message = 'Tarefa removida!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onDeleteTask(task) {
      this.removeTask(task.id);
    },
  },
  created() {
    this.getTasks();
  },
};
</script>

<template>
  <div class="movie-add-form">
    <h3>Yangi kino qo'shish</h3>
    <form class="add-form d-flex" @submit.prevent="addMovie">
      <Input 
      class="new-movie-label"  
      placeholder="Qanday kino?" 
      v-model="name" 
      @input="name = $event.target.value"/>
      <input
        type="number"
        class="form-control new-movie-label"
        placeholder="Necha marotaba ko'rilgan?"
        v-model="viewers"
        autocomplete="off"
       
      />
    
      <PrimaryButton class="btn-outline-dark" type="submit">
        Qo'shish
      </PrimaryButton>
    </form>
  </div>
</template>

<script>
import Input from '../ui-components/Input.vue';
import PrimaryButton from '../ui-components/PrimaryButton.vue';


export default {


  data() {
    return {
      name: '',
      viewers: '',
    }
  },
  components: {
    Input,
    PrimaryButton
  },
  methods: {
    addMovie() {
      if (!this.name || this.viewers === '') return
      this.$emit('createMovie', {
        name: this.name,
        viewers: Number(this.viewers),
        favourite: false,
        like: false,

      })
      this.name = ''
      this.viewers = ''
    },
  },
}
</script>
 
<style>
.movie-add-form{
  margin-top: 2rem;
  margin-bottom: 1rem;
  padding: 1.5rem;
  background-color: #fcfaf5;
  border-radius: 4px;
  box-shadow: 15px 15px 15px rgba(0, 0, 0, 0.15);
}

</style>
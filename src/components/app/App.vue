<template>
  <div class="app font-monospace">
    <div class="content">
      <AppInfo
        :allMoviesCount="allMovies.length"
        :favouriteMoviesCount="moviesWithState.filter(c => c.favourite).length"
      />
      <div class="search-panel">
        <SearchPanel :updateTermHandler="updateTermHandler" />
        <AppFilter :updaterFilterHandler="updateFilterHandler" :filterName="filter" />
      </div>

      <Box v-if="!movies.length && !isLoading">
        <p class="text-center fs-3 text-denger">Hozircha kinolar yo'q</p>
      </Box>
      <Box v-else-if="isLoading" class="d-flex justify-content-center">
        <Loader />
      </Box>
      <MovieList
        v-else
        :movies="movies"
        @onToggle="onToggleHandler"
        @onRemove="onRemoveHandler"
      />

      <Box class="d-flex justify-content-center">
        <nav aria-label="pagination">
          <ul class="pagination">
            <li
              v-for="pageNumber in totalPages"
              :key="pageNumber"
              :class="{ active: pageNumber === page }"
              @click="changePageHandler(pageNumber)"
            >
              <span class="page-link">{{ pageNumber }}</span>
            </li>
          </ul>
        </nav>
      </Box>

      <MovieAddForm @createMovie="createMovie" />
    </div>
  </div>
</template>

<script>
import AppInfo from '../app-info/AppInfo.vue'
import SearchPanel from '../search-panel/SearchPanel.vue'
import AppFilter from '../app-filter/AppFilter.vue'
import MovieList from '../movie-list/Movie.list.vue'
import MovieAddForm from '../movie-add-form/MovieAddForm.vue'
import axios from 'axios'
import Loader from '../ui-components/Loader.vue'
import Box from '../ui-components/Box.vue'

export default {
  components: {
    AppInfo,
    SearchPanel,
    AppFilter,
    MovieList,
    MovieAddForm,
    Loader,
    Box,
  },

  data() {
    return {
      allMovies: [],
      term: '',
      filter: 'all',
      isLoading: false,
      limit: 10,
      page: 1,
      savedState: {},
    }
  },

  computed: {
    moviesWithState() {
      return this.allMovies.map(m => ({ ...m, ...this.savedState[m.id] }))
    },
    filteredMovies() {
      return this.onFilterHandler(
        this.onSearchHandler(this.moviesWithState, this.term),
        this.filter
      )
    },
    totalPages() {
      return Math.ceil(this.filteredMovies.length / this.limit)
    },
    movies() {
      const start = (this.page - 1) * this.limit
      return this.filteredMovies.slice(start, start + this.limit)
    },
  },

  methods: {
    async createMovie(item) {
      try {
        await axios.post('https://jsonplaceholder.typicode.com/posts', item)
        const lastId = this.allMovies.reduce((max, m) => Math.max(max, m.id), 0)
        this.allMovies.push({
          like: false,
          favourite: false,
          viewers: 0,
          ...item,
          id: lastId + 1,
        })
        this.filter = 'all'
        this.term = ''
        this.$nextTick(() => {
          this.page = this.totalPages
        })
      } catch (error) {
        alert(error.message)
      }
    },

    onToggleHandler({ id, prop }) {
      const current = this.moviesWithState.find(m => m.id === id)
      this.savedState = {
        ...this.savedState,
        [id]: { ...this.savedState[id], [prop]: !current[prop] },
      }
    },

    async onRemoveHandler(id) {
      try {
        await axios.delete(`https://jsonplaceholder.typicode.com/posts/${id}`)
        this.allMovies = this.allMovies.filter(c => c.id !== id)
      } catch (error) {
        alert(error.message)
      }
    },

    onSearchHandler(arr, term) {
      if (term.length === 0) {
        return arr
      }
      return arr.filter(c => c.name.toLowerCase().indexOf(term.toLowerCase()) > -1)
    },

    onFilterHandler(arr, filter) {
      switch (filter) {
        case 'popular':
          return arr.filter(c => c.like)
        case 'mostViewers':
          return arr.filter(c => c.viewers > 500)
        default:
          return arr
      }
    },

    updateTermHandler(term) {
      this.term = term
    },

    updateFilterHandler(filter) {
      this.filter = filter
    },

    changePageHandler(page) {
      this.page = page
    },

    async fetchMovie() {
      try {
        this.isLoading = true
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts')
        this.allMovies = response.data.map(item => ({
          id: item.id,
          name: item.title,
          like: false,
          favourite: false,
          viewers: item.id * 10,
        }))
      } catch (error) {
        alert(error.message)
      } finally {
        this.isLoading = false
      }
    },
  },

  mounted() {
    this.fetchMovie()
  },

  watch: {
    filter() {
      this.page = 1
    },
    term() {
      this.page = 1
    },
  },
}
</script>

<style>
.app {
  height: 100vh;
  color: #000;
}
.content {
  width: 1000px;
  min-height: 700px;
  background-color: #fff;
  margin: 0 auto;
  padding: 5rem 0;
}
.search-panel {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #fcfaf5;
  border-radius: 4px;
  box-shadow: 15px 15px 15px rgba(0, 0, 0, 0.15);
}
</style>
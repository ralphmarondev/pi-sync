import { defineStore } from 'pinia'

export interface State {
  count: number
}

export const useStore = defineStore('store', {
  state: (): State => ({
    count: 0
  }),
  actions: {
    increment() {
      this.count++
      console.log('incremented', this.count)
    }
  }
})
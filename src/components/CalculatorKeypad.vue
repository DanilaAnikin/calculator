<template>
    <div class="grid grid-cols-6 gap-2">
      <template v-for="(row, rowIndex) in computedKeys" :key="rowIndex">
        <template v-for="(btn, btnIndex) in row" :key="btnIndex">
          <CalculatorKey
            :label="btn.label"
            :value="btn.value"
            :colSpan="btn.colSpan"
            @button-click="$emit('button-click', $event)"
          />
        </template>
      </template>
    </div>
</template>  

<script setup lang="ts">
import CalculatorKey from './CalculatorKey.vue';
import { defineEmits, defineProps, computed, ref } from 'vue';

const emit = defineEmits<{ (e: 'button-click', value: string): void }>();

const baseKeys = ref([
    [
      { label: 'xʸ', value: '^' },
      { label: 'x!', value: '!' },
      { label: '(', value: '(' },
      { label: ')', value: ')' },
      { label: '%', value: '/100' },
      { label: 'AC', value: 'AC' }
    ],
    [
      { label: 'sin', value: 'sin(' },
      { label: 'ln', value: 'ln(' },
      { label: '7', value: '7' },
      { label: '8', value: '8' },
      { label: '9', value: '9' },
      { label: '/', value: '/' }
    ],
    [
      { label: 'cos', value: 'cos(' },
      { label: 'log', value: 'log10(' },
      { label: '4', value: '4' },
      { label: '5', value: '5' },
      { label: '6', value: '6' },
      { label: '×', value: '*' }
    ],
    [
      { label: 'tan', value: 'tan(' },
      { label: '√', value: 'sqrt(' },
      { label: '1', value: '1' },
      { label: '2', value: '2' },
      { label: '3', value: '3' },
      { label: '-', value: '-' }
    ],
    [
      { label: 'e', value: 'e' },
      { label: 'π', value: 'pi' },
      { label: '0', value: '0' },
      { label: '.', value: '.' },
      { label: '=', value: '=' },
      { label: '+', value: '+' }
    ],
]);
  
const computedKeys = computed(() => {
    const keysCopy = JSON.parse(JSON.stringify(baseKeys.value)) as typeof baseKeys.value;
    
    return keysCopy;
});
</script>

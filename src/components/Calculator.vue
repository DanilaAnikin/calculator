<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <div class="w-fit bg-white rounded-lg shadow-lg p-4">
        <CalculatorDisplay :expression="expression" />
        <CalculatorKeypad :angleMode="angleMode" @button-click="handleKeyPress" />
      </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { evaluate } from 'mathjs';
import CalculatorDisplay from './CalculatorDisplay.vue';
import CalculatorKeypad from './CalculatorKeypad.vue';

const expression = ref('');

const handleKeyPress = (value: string) => {
    if (value === 'AC') {
      expression.value = '';
    } else if (value === '=') {
      try {
        const result = evaluate(expression.value);
        expression.value = result.toString();
      } catch {
        expression.value = 'Error';
      }
    } else {
      expression.value += value;
    }
};
</script>
  
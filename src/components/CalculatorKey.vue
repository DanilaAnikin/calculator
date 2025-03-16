<template>
    <button
      @click="handleClick"
      class="px-5 py-3 border border-gray-400 text-gray-950 rounded-xl hover:bg-gray-200"
    >
      <span>{{ label }}</span>
    </button>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, computed } from 'vue';

const props = defineProps<{ label: string; value: string; colSpan?: number }>();
const emit = defineEmits<{ (e: 'button-click', value: string): void }>();

const handleClick = () => {
    emit('button-click', props.value);
};
</script>
  
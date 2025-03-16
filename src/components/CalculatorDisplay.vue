<template>
    <input
      type="text"
      :value="expression"
      readonly
      class="w-full p-2 border border-gray-300 rounded mb-2 text-right"
    />
</template>

<script setup lang="ts">
const props = defineProps<{ expression: string }>();
</script>
  
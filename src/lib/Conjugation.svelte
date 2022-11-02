<script>
  export let pronoun;
  export let isCorrect;
  export let value;
  export let inputRef = null;
  export let revealAnswer;
</script>

<div class="relative mb-8 flex flex-row text-4xl" class:bg-lime-300={isCorrect}>
  <span
    class="inline-flex items-center rounded-l-md border border-r-0 border-gray-300  px-3 text-4xl text-gray-900 "
  >
    {pronoun}
  </span>
  <input
    bind:value
    class="block w-full min-w-0 flex-1 rounded-none rounded-r-lg border border-gray-300 p-2.5 text-4xl text-gray-900 focus:border-blue-500 focus:ring-blue-500  "
    class:bg-lime-300={isCorrect}
    bind:this={inputRef}
  />
  {#if !isCorrect}
    <button
      type="submit"
      class="absolute right-2.5 bottom-3.5 bg-black px-2 py-2 text-sm font-medium text-white"
      on:click={revealAnswer}>Show</button
    >
  {/if}
</div>

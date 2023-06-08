<script>
  export let pronoun;
  export let isCorrect;
  export let value;
  export let inputRef = null;
  export let revealAnswer;
</script>

<div class="relative mb-8 flex flex-row text-4xl" class:bg-lime-200={isCorrect}>
  <span
    class="inline-flex items-center rounded-l-md border-0 border-r-0 border-black bg-gray-200 px-3 text-4xl text-gray-900"
  >
    {pronoun}
  </span>
  <input
    bind:value
    class="focus:border-1 block w-full min-w-0 flex-1 rounded-none rounded-r-lg border-black p-2.5 text-4xl text-gray-900"
    class:bg-green-500={isCorrect}
    class:bg-gray-100={!isCorrect}
    bind:this={inputRef}
  />
  {#if !isCorrect}
    <button
      type="submit"
      class="absolute right-2.5 bottom-3.5 rounded-md bg-black px-2 py-2 text-sm font-medium text-white"
      on:click={revealAnswer}>Révéler</button
    >
  {/if}
</div>

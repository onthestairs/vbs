<script>
  export let pronoun;
  export let isCorrect;
  export let value;
  export let inputRef = null;
</script>

<div class="mb-8 flex flex-row" class:bg-lime-300={isCorrect}>
  {pronoun}
  <input
    bind:value
    class="w-500 w-lg ml-4 border-b-2"
    class:bg-lime-300={isCorrect}
    bind:this={inputRef}
  />
</div>

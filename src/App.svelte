<script>
  import verbs from "./data/verbs.json";
  import Verb from "./lib/Verb.svelte";
  let verbIndex = 1;
  const randomise = () => {
    verbIndex = Math.floor(Math.random() * verbs.length);
  };
  $: verb = verbs[verbIndex];
</script>

<main class="mx-auto mt-16 max-w-md font-garamond">
  <div>
    <Verb {verb} />
    <button
      class="rounded-full bg-lime-500 px-4 py-2 text-sm font-semibold text-white shadow-sm"
      on:click={randomise}
    >
      Next
    </button>
  </div>
</main>

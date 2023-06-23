<script>
  import ConjugationApp from "./lib/conjugation/App.svelte";
  import OralApp from "./lib/oral/App.svelte";
  import { path, query, fragment, pattern } from "svelte-pathfinder";
  let params;
</script>

{#if (params = $pattern("/conjugation"))}
  <ConjugationApp />
{:else if (params = $pattern("/oral"))}
  <OralApp />
{:else}
  <p>Not found</p>
{/if}

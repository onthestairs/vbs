<script>
  import ConjugationApp from "./lib/conjugation/App.svelte";
  import OralApp from "./lib/oral/App.svelte";
  import { path, query, fragment, pattern } from "svelte-pathfinder";
  let params;
  // go to conjugation by default
  if ((params = $pattern("/"))) {
    $path = "/conjugation";
  }
  const titleFromPattern = ($pattern) => {
    if ((params = $pattern("/conjugation"))) {
      return "La Conjugaison Française";
    } else if ((params = $pattern("/pronunciation"))) {
      return "La prononciation Française";
    }
    return "Apprendre le français";
  };
  $: {
    document.title = titleFromPattern($pattern);
  }
</script>

{#if (params = $pattern("/conjugation"))}
  <ConjugationApp />
{:else if (params = $pattern("/pronunciation"))}
  <OralApp />
{:else}
  <p>Not found</p>
{/if}

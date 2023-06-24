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
    return null;
  };
  $: {
    const title = titleFromPattern($pattern);
    if (title !== null) {
      document.title = title;
    }
  }
  const navs = [
    { text: "Conjugasion", path: ["conjugation"] },
    { text: "Prononciation", path: ["pronunciation"] },
  ];
</script>

{#if (params = $pattern("/conjugation"))}
  <ConjugationApp />
{:else if (params = $pattern("/pronunciation"))}
  <OralApp />
{:else}
  <p>Not found</p>
{/if}

<nav class="fixed top-0 left-0 mt-4 ml-4 font-garamond">
  <ul>
    {#each navs as nav}
      <li>
        <a
          href={nav.path.join("/")}
          class="text-gray-500 hover:text-black"
          on:click={(e) => {
            e.preventDefault();
            $path = nav.path;
            $query = {};
          }}
        >
          {nav.text}
        </a>
      </li>
    {/each}
  </ul>
</nav>

<script>
  import ConjugationApp from "./lib/conjugation/App.svelte";
  import OralApp from "./lib/oral/App.svelte";
  import PrepositionsApp from "./lib/prepositions/App.svelte";
  import deepEqual from "deep-equal";
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
    } else if ((params = $pattern("/prepositions"))) {
      return "Les prépositions Françaises";
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
    { text: "Conjugaison", path: ["conjugation"] },
    { text: "Prononciation", path: ["pronunciation"] },
    { text: "Prépositions", path: ["prepositions"] },
  ];
</script>

{#if (params = $pattern("/conjugation"))}
  <ConjugationApp />
{:else if (params = $pattern("/pronunciation"))}
  <OralApp />
{:else if (params = $pattern("/prepositions"))}
  <PrepositionsApp />
{:else}
  <p>Not found</p>
{/if}

<nav class="fixed top-0 left-0 mt-4 ml-4 font-garamond">
  <ul>
    {#each navs as nav}
      <li>
        {#if !deepEqual(nav.path, $path)}
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
        {:else}
          <p class="font-bold text-black ">{nav.text}</p>
        {/if}
      </li>
    {/each}
  </ul>
</nav>

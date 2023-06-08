<script>
  import { query } from "svelte-pathfinder";

  import verbs from "./data/verbs.json";
  import top100 from "./data/top-100.json";
  import group2 from "./data/2e-groupe.json";
  import group3 from "./data/3e-groupe.json";
  import Verb from "./lib/Verb.svelte";

  let allInfinitives = verbs.map((verb) => verb.infinitive);
  let topNChoices = [10, 20, 50, 100];

  const omit = (o, k) => {
    let newK = {};
    for (let l in o) {
      if (l !== k) {
        newK[l] = o[l];
      }
    }
    return newK;
  };

  $query.verbs = $query.verbs || "top20";

  $: if ($query.verbs != "custom") {
    $query = omit($query, "customRegex");
  }
  let customRegexInput;
  const onCustomRegexBlur = () => {
    $query.customRegex = customRegexInput;
  };
  let filterInfinitives = (verbs, customRegex) => {
    if (verbs === "all") {
      return allInfinitives;
    }
    if (verbs === "custom") {
      const re = new RegExp(customRegex);
      return allInfinitives.filter((verb) => {
        return verb.match(re);
      });
    }
    if (verbs === "1er") {
      return allInfinitives.filter((verb) => {
        return !(group2.includes(verb) || group3.includes(verb));
      });
    }
    if (verbs === "2e") {
      return allInfinitives.filter((verb) => {
        return group2.includes(verb);
      });
    }
    if (verbs === "3e") {
      return allInfinitives.filter((verb) => {
        return group3.includes(verb);
      });
    }
    const topPrefix = "top";
    if (verbs.startsWith(topPrefix)) {
      const trimmed = verbs.substring(topPrefix.length);
      const n = parseInt(trimmed);
      return top100.slice(0, n);
    }
    return allInfinitives;
  };
  $: goodInfinitives = filterInfinitives($query.verbs, $query.customRegex);
  let filteredVerbs = verbs;
  $: filteredVerbs = verbs.filter((verb) =>
    goodInfinitives.includes(verb.infinitive)
  );

  let indicativePresent = "indicative-present";
  let indicativeImperfect = "indicative-imperfect";
  let indicativeFuture = "indicative-future";
  let subjunctivePresent = "subjunctive-present";
  let subjunctiveImperfect = "subjunctive-imperfect";
  let verbForms =
    $query.verbForms !== undefined
      ? $query.verbForms.split("|")
      : [indicativePresent];
  $: verbForms = $query.verbForms.split("|");
  $: $query.verbForms = verbFormInputs.join("|");

  let verbFormInputs = verbForms;

  $: verbIndex = Math.floor(Math.random() * filteredVerbs.length);
  const randomiseVerb = () => {
    verbIndex = Math.floor(Math.random() * filteredVerbs.length);
  };
  let verb = filteredVerbs[verbIndex];
  $: verb = filteredVerbs[verbIndex];

  $: verbFormIndex = Math.floor(Math.random() * verbForms.length);
  const randomiseVerbForm = () => {
    verbFormIndex = Math.floor(Math.random() * verbForms.length);
  };
  let verbForm = verbForms[verbFormIndex];
  $: verbForm = verbForms[verbFormIndex];

  const randomise = () => {
    randomiseVerb();
    randomiseVerbForm();
  };

  let nextButton;
  let allCorrect;
  $: if (allCorrect) {
    nextButton.focus();
  }
  $: nextButtonText = allCorrect ? "Suivant" : "Passer";
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div class="mb-12 mt-4 flex flex-col justify-between ">
    <h2 class="m-auto text-3xl font-bold underline">
      🇫🇷 La conjugaison française 🇫🇷
    </h2>
    <div class="mt-8 flex items-center justify-center">
      <div class="grid grid-cols-2 gap-4">
        <div class="rounded-md bg-violet-100 p-2">
          <h3 class="font-bold">Verbes</h3>
          {#each topNChoices as choice}
            <label class="mr-2">
              <input
                type="radio"
                bind:group={$query.verbs}
                name="topN"
                value={`top${choice}`}
              />
              Top {choice}
            </label>
          {/each}
          <label class="mr-2">
            <input
              type="radio"
              bind:group={$query.verbs}
              name="topN"
              value={`all`}
            />
            Tous
          </label>
          <br />

          <label class="mr-2">
            <input
              type="radio"
              bind:group={$query.verbs}
              name="1er"
              value={"1er"}
            />
            1er groupe
          </label>
          <label class="mr-2">
            <input
              type="radio"
              bind:group={$query.verbs}
              name="2e"
              value={"2e"}
            />
            2e groupe
          </label>
          <label class="mr-2">
            <input
              type="radio"
              bind:group={$query.verbs}
              name="3e"
              value={"3e"}
            />
            3e groupe
          </label>

          <br />
          <label class="mr-2">
            <input
              type="radio"
              bind:group={$query.verbs}
              name="topN"
              value={"custom"}
            />
            Custom
          </label>
          <input
            bind:value={customRegexInput}
            on:focus={() => ($query.verbs = "custom")}
            on:blur={onCustomRegexBlur}
          />
        </div>
        <div class="rounded-md bg-teal-100 p-2">
          <h3 class="font-bold">Mode/Tense</h3>
          <div class="grid grid-cols-2 gap-2 ">
            <div>
              <label>
                <input
                  type="checkbox"
                  bind:group={verbFormInputs}
                  name="tenses"
                  value={indicativePresent}
                  disabled={verbForms.length == 1 &&
                    verbForms[0] == indicativePresent}
                />
                Indicatif/Présent
              </label><br />
              <label>
                <input
                  type="checkbox"
                  bind:group={verbFormInputs}
                  name="tenses"
                  value={indicativeImperfect}
                  disabled={verbForms.length == 1 &&
                    verbForms[0] == indicativeImperfect}
                />
                Indicatif/Imparfait
              </label>
              <br />
              <label>
                <input
                  type="checkbox"
                  bind:group={verbFormInputs}
                  name="tenses"
                  value={indicativeFuture}
                  disabled={verbForms.length == 1 &&
                    verbForms[0] == indicativeFuture}
                />
                Indicatif/Futur
              </label>
            </div>
            <div>
              <label>
                <input
                  type="checkbox"
                  bind:group={verbFormInputs}
                  name="tenses"
                  value={subjunctivePresent}
                  disabled={verbForms.length == 1 &&
                    verbForms[0] == subjunctivePresent}
                />
                Subjonctif/Présent
              </label>
              <br />
              <label>
                <input
                  type="checkbox"
                  bind:group={verbFormInputs}
                  name="tenses"
                  value={subjunctiveImperfect}
                  disabled={verbForms.length == 1 &&
                    verbForms[0] == subjunctiveImperfect}
                />
                Subjonctif/Imperfait
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  {#if verb !== undefined}
    <div>
      <Verb {verb} {verbForm} bind:allCorrect />
    </div>
    <div class="mt-4 flex items-center justify-center">
      <div>
        <input
          type="button"
          value={nextButtonText}
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          on:click={randomise}
          bind:this={nextButton}
        />
      </div>
    </div>
  {:else}
    No matching verbs
  {/if}
</main>

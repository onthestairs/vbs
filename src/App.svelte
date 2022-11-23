<script>
  import verbs from "./data/verbs.json";
  import top100 from "./data/top-100.json";
  import Verb from "./lib/Verb.svelte";

  let allInfinitives = verbs.map((verb) => verb.infinitive);
  let topNChoices = [10, 20, 50, 100, null];
  let topN = 20;
  let customRegex, customRegexInput;
  const onCustomRegexBlur = () => {
    customRegex = customRegexInput;
  };
  let filterInfinitives = (topN, customRegex) => {
    if (topN === null) {
      return allInfinitives;
    }
    if (topN === "custom") {
      const re = new RegExp(customRegex);
      return top100.filter((verb) => {
        return verb.match(re);
      });
    }
    return top100.slice(0, topN);
  };
  $: goodInfinitives = filterInfinitives(topN, customRegex);
  let filteredVerbs = verbs;
  $: filteredVerbs = verbs.filter((verb) =>
    goodInfinitives.includes(verb.infinitive)
  );

  let indicativePresent = ["indicative", "present"];
  let indicativeImperfect = ["indicative", "imperfect"];
  let verbForms = [indicativePresent];

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
  $: nextButtonText = allCorrect ? "Next" : "Skip";
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div class="mb-12 mt-4 flex flex-row justify-between border-b-2 border-black">
    <h2 class="pb-4 text-3xl font-bold">La conjugaison française 🇫🇷</h2>
    <div class="flex flex-row">
      <div class="mr-8">
        {#each topNChoices as choice}
          <label class="mr-2">
            <input type="radio" bind:group={topN} name="topN" value={choice} />
            {#if choice === null}
              All
            {:else}
              Top {choice}
            {/if}
          </label>
        {/each}
        <br />
        <label class="mr-2">
          <input type="radio" bind:group={topN} name="topN" value={"custom"} />
          Custom
        </label>
        <input bind:value={customRegexInput} on:blur={onCustomRegexBlur} />
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            bind:group={verbForms}
            name="tenses"
            value={indicativePresent}
            disabled={verbForms.length == 1 &&
              verbForms[0] == indicativePresent}
          />
          Indicative/Present
        </label><br />
        <label>
          <input
            type="checkbox"
            bind:group={verbForms}
            name="tenses"
            value={indicativeImperfect}
            disabled={verbForms.length == 1 &&
              verbForms[0] == indicativeImperfect}
          />
          Indicative/Imperfect
        </label>
      </div>
    </div>
  </div>
  <div>
    <Verb {verb} {verbForm} bind:allCorrect />
  </div>
  <div class="mt-8 flex items-center justify-center">
    <div>
      <input
        type="button"
        value={nextButtonText}
        class="cursor-pointer bg-black px-4 py-2 text-4xl font-semibold text-white "
        on:click={randomise}
        bind:this={nextButton}
      />
    </div>
  </div>
</main>

<script>
  import verbs from "./data/verbs.json";
  import top100 from "./data/top-100.json";
  import Verb from "./lib/Verb.svelte";

  let allInfinitives = verbs.map((verb) => verb.infinitive);
  let topN = 20;
  let defaultVerbForm = ["indicative", "present"];
  let verbForms = [defaultVerbForm];
  $: console.log(verbForms);
  $: goodInfinitives = topN === null ? allInfinitives : top100.slice(0, topN);
  let filteredVerbs = verbs;
  $: filteredVerbs = verbs.filter((verb) =>
    goodInfinitives.includes(verb.infinitive)
  );

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
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div
    class="mb-12 mt-12 flex flex-row justify-between border-b-2 border-black"
  >
    <h2 class="text-3xl font-bold">French conjugation</h2>
    <div class="flex flex-col">
      <div>
        <label>
          <input type="radio" bind:group={topN} name="topN" value={10} />
          Top 10
        </label>

        <label>
          <input type="radio" bind:group={topN} name="topN" value={20} />
          Top 20
        </label>

        <label>
          <input type="radio" bind:group={topN} name="topN" value={50} />
          Top 50
        </label>

        <label>
          <input type="radio" bind:group={topN} name="topN" value={100} />
          Top 100
        </label>

        <label>
          <input type="radio" bind:group={topN} name="topN" value={null} />
          All
        </label>
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            bind:group={verbForms}
            name="tenses"
            value={defaultVerbForm}
          />
          Indicative/Present
        </label>
        <label>
          <input
            type="checkbox"
            bind:group={verbForms}
            name="tenses"
            value={["indicative", "imperfect"]}
          />
          Indicative/Imperfect
        </label>
      </div>
    </div>
    <div>
      <button
        class="bg-black px-4 py-2 text-sm font-semibold text-white "
        on:click={randomise}
      >
        Next
      </button>
    </div>
  </div>
  <div>
    <Verb {verb} {verbForm} />
  </div>
</main>

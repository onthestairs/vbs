<script>
  import prepositions from "../../data/prepositions/prepositions.json";
  $: index = Math.floor(Math.random() * prepositions.length);
  const getFreshIndex = () => {
    while (true) {
      const newIndex = Math.floor(Math.random() * prepositions.length);
      if (newIndex !== index) {
        return newIndex;
      }
    }
  };
  const nextPreposition = () => {
    index = getFreshIndex();
    currentAnswer = null;
  };
  let currentAnswer = null;
  const setCurrentAnswer = (answer) => {
    currentAnswer = answer;
  };
  $: currentPreposition = prepositions[index];
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div class="mb-12 mt-4 flex flex-col justify-between ">
    <h2 class="m-auto text-3xl font-bold underline">
      🇫🇷 Les prépositions françaises 🇫🇷
    </h2>
  </div>
  <div class="mt-16">
    <div class="flex flex-col items-center justify-center">
      <div class="text-6xl">
        {#each currentPreposition.french as part}
          {#if part !== null}
            <span>{part}</span>
          {:else if currentAnswer !== null}
            {#if currentAnswer === currentPreposition.answer}
              {" "}<span class="text-green-800">{currentAnswer} </span>{" "}
            {:else}
              {" "}<span class="text-red-800 line-through">{currentAnswer}</span
              >{" "}
              <span class="text-green-800">{currentPreposition.answer}</span
              >{" "}
            {/if}
          {:else}
            <span>{" "}___{" "}</span>
          {/if}
        {/each}
      </div>
      <div class="mt-8 text-2xl italic text-gray-500">
        {currentPreposition.english}
      </div>
      <div class="mt-8 flex gap-6 text-6xl">
        {#if currentAnswer !== null}
          <button
            class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white"
            on:click={(_e) => nextPreposition()}
          >
            Suivant
          </button>
        {:else}
          {#each currentPreposition.options as option}
            <button
              class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white"
              on:click={(_e) => setCurrentAnswer(option)}
              >{option}
            </button>
          {/each}
        {/if}
      </div>
    </div>
  </div>
</main>

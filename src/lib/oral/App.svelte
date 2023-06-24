<script>
  import oralSets from "../../data/oral/sets.json";
  let currentWord;
  let repetitions = 5;
  let bufferSeconds = 0.5;
  let queue = [];
  let filteredSets = oralSets;
  let currentSet;
  $: setsIndex = Math.floor(Math.random() * filteredSets.length);
  $: currentSet = filteredSets[setsIndex];

  const newSet = () => {
    queue = [];
    const findNewIndex = () => {
      const index = Math.floor(Math.random() * filteredSets.length);
      if (index !== setsIndex) {
        return index;
      } else {
        return findNewIndex();
      }
    };
    console.log(`Setting index to ${setsIndex}`);
    setsIndex = findNewIndex();
  };

  const makeAudioFile = (word) => {
    return `/oral/audio/${word}.mp3`;
  };

  const runQueue = () => {
    let word = queue.shift();
    if (word !== undefined) {
      const url = makeAudioFile(word);
      let audio = new Audio(url);
      audio.onended = () => {
        const delay = audio.duration + bufferSeconds;
        console.log(`Delaying for ${delay}`);
        setTimeout(() => runQueue(), 1000 * delay);
      };
      currentWord = word;
      audio.play();
    } else {
      setTimeout(runQueue, 100);
    }
  };
  runQueue();

  const resetQueue = () => {
    queue = [];
    currentWord = null;
  };

  const enqueueSet = (set) => {
    let toQueue = [];
    for (let i = 0; i < repetitions; i++) {
      set.forEach((word) => {
        toQueue.push(word);
      });
    }
    queue = toQueue;
  };
</script>

<main class="mx-auto max-w-5xl font-garamond">
  <div class="mb-12 mt-4 flex flex-col justify-between ">
    <h2 class="m-auto text-3xl font-bold underline">🇫🇷 Oral française 🇫🇷</h2>
  </div>
  <div class="mt-8 flex items-center justify-center">
    <div class="grid grid-cols-2 gap-4">
      <div class="rounded-md bg-violet-100 p-2">
        <h3 class="font-bold">Optiones</h3>
        <label class="mr-2">
          Repetitions:
          <input type="number" bind:value={repetitions} />
        </label>
      </div>
    </div>
  </div>
  <div class="mt-32">
    <div class="flex justify-center gap-12">
      {#each currentSet as word}
        {#if word == currentWord}
          <div class="text-6xl font-bold text-red-600">{word}</div>
        {:else}
          <div class="text-6xl font-bold text-blue-600">{word}</div>
        {/if}
      {/each}
    </div>
    <div class="mt-4 flex items-center justify-center">
      {#if queue.length === 0}
        <input
          type="button"
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          value="Play"
          on:click={() => enqueueSet(currentSet)}
        />
      {:else}
        <input
          type="button"
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          value="Stop"
          on:click={() => resetQueue()}
        />
      {/if}
      <input
        type="button"
        class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
        value="Passer a l'autre set"
        on:click={() => newSet()}
      />
    </div>
  </div>
</main>

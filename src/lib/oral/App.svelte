<script>
  import oralSets from "../../data/oral/sets.json";
  let currentWord;
  let repetitions = 5;
  let autoskip = false;
  let bufferSeconds = 0.5;
  let queue = [];
  let filteredSets = oralSets;
  let currentSet;
  let addToQueue = false;
  let currentAudio = null;
  $: setsIndex = Math.floor(Math.random() * filteredSets.length);
  $: currentSet = filteredSets[setsIndex];
  $: repetitionsToCome =
    queue.length > 0
      ? Math.floor((queue.length - 1) / currentSet.length)
      : undefined;
  $: if (addToQueue) {
    enqueueSet(currentSet);
    addToQueue = false;
  }
  $: playNext(queue);

  const playNext = (words) => {
    if (words.length > 0) {
      const [word, ...nextWords] = queue;
      const url = makeAudioFile(word);
      let audio = new Audio(url);
      audio.onended = () => {
        currentAudio = null;
        const delay = audio.duration + bufferSeconds;
        console.log(`Delaying for ${delay}`);
        setTimeout(() => {
          if (nextWords.length === 0 && autoskip) {
            newSet();
            addToQueue = true;
          } else {
            // i.e. if the queue hasn't been interfered with in the meantimme
            if (queue === words) {
              queue = nextWords;
            }
          }
        }, 1000 * delay);
      };
      currentWord = word;
      currentAudio = audio;
      audio.play();
    } else {
      currentWord = null;
    }
  };

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

  const resetQueue = () => {
    queue = [];
    currentWord = null;
  };

  const stop = () => {
    if (currentAudio !== null) {
      currentAudio.pause();
      currentAudio = null;
    }
    resetQueue();
  };

  const enqueueSet = (set) => {
    console.log("adding", set);
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
    <h2 class="m-auto text-3xl font-bold underline">
      🇫🇷 La prononciation française 🇫🇷
    </h2>
  </div>
  <div class="mt-8 flex items-center justify-center">
    <div class="grid grid-cols-2 gap-4">
      <div class="rounded-md bg-violet-100 p-2">
        <h3 class="font-bold">Options</h3>
        <div>
          <label class="mr-2">
            Répétitions:
            <input type="number" min="" bind:value={repetitions} />
          </label>
        </div>
        <div>
          <label class="mr-2">
            Passer automatiquement:
            <input type="checkbox" bind:checked={autoskip} />
          </label>
        </div>
      </div>
      <div class="rounded-md bg-teal-100 p-2">
        <h3 class="font-bold">Groupes</h3>
        {#each oralSets as set}
          <label class="mr-2 inline-block">
            <input
              type="checkbox"
              bind:group={filteredSets}
              value={set}
              disabled={filteredSets.length === 1 && filteredSets[0] === set}
            />
            {set.join("/")}
          </label>
        {/each}
      </div>
    </div>
  </div>
  <div class="mt-32">
    <div class="flex justify-center">
      <div class="text-2xl ">Répétez après chaque mot</div>
    </div>
    <div class="mt-16 flex justify-center gap-12">
      {#each currentSet as word}
        {#if word == currentWord}
          <div class="text-6xl font-bold text-red-600">{word}</div>
        {:else}
          <div class="text-6xl font-bold text-blue-600">{word}</div>
        {/if}
      {/each}
    </div>
    <div class="mt-32 flex items-center justify-center">
      {#if queue.length === 0}
        <input
          type="button"
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          value="Jouer"
          on:click={() => {
            addToQueue = true;
          }}
        />
      {:else}
        <input
          type="button"
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          value="Arrêter"
          on:click={() => stop()}
        />
      {/if}
    </div>
    <div class="mt-4 flex items-center justify-center">
      {#if filteredSets.length > 1}
        <input
          type="button"
          class="cursor-pointer rounded-md bg-black px-4 py-2 text-4xl font-semibold text-white "
          value="Passer a l'autre groupe"
          on:click={() => newSet()}
        />
      {/if}
    </div>
  </div>
</main>

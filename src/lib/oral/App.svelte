<script>
  import oralSets from "../../data/oral/sets.json";
  let currentWord;
  let maxIterations = 5;
  let bufferSeconds = 0.5;
  let queue = [];

  const makeAudioFile = (word) => {
    return `/public/oral/audio/${word}.mp3`;
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
    for (let i = 0; i < maxIterations; i++) {
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
  {#each oralSets as set}
    <div>
      {#if queue.length === 0}
        <input type="button" value="Play" on:click={() => enqueueSet(set)} />
      {:else}
        <input type="button" value="Stop" on:click={() => resetQueue()} />
      {/if}
      {#each set as word}
        {#if word == currentWord}
          <p class="text-6xl font-bold text-red-600">{word}</p>
        {:else}
          <p class="text-6xl font-bold text-blue-600">{word}</p>
        {/if}
      {/each}
    </div>
  {/each}
</main>

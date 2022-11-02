<script>
  import verbs from "./data/verbs.json";
  import Verb from './lib/Verb.svelte'
  let verbIndex = 1;
  const randomise = () => {
	  verbIndex = Math.floor(Math.random() * verbs.length);
  }
  $: verb = verbs[verbIndex];
</script>

<main>

  <div >
	<button on:click={randomise}>
	  New verb
	</button>
    <Verb verb={verb}/>
  </div>

</main>

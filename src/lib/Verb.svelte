<script>
  export let verb;
  let first_person_singular = "";
  let second_person_singular= "";
  let third_person_singular = "";
  let first_person_plural= "";
  let second_person_plural= "";
  let third_person_plural= "";
  $: first_person_singular_correct = first_person_singular === verb.indicative.present.first_person_singular;
  $: second_person_singular_correct = second_person_singular === verb.indicative.present.second_person_singular;
  $: third_person_singular_correct = third_person_singular === verb.indicative.present.third_person_singular;
  $: first_person_plural_correct = first_person_plural === verb.indicative.present.first_person_plural;
  $: second_person_plural_correct = second_person_plural === verb.indicative.present.second_person_plural;
  $: third_person_plural_correct = third_person_plural === verb.indicative.present.third_person_plural;
</script>


<h1 class="text-5xl font-bold italic underline">{verb.infinitive}</h1>

<div>
  <div>Je <input bind:value={first_person_singular} class:correct="{first_person_singular_correct}" ></div>

	<div>Tu <input bind:value={second_person_singular} class:correct="{second_person_singular_correct}" ></div>
  <div>Il/Elle/On <input bind:value={third_person_singular} class:correct="{third_person_singular_correct}" ></div>
  <div>Nous <input bind:value={first_person_plural} class:correct="{first_person_plural_correct}" ></div>
  <div>Vous <input bind:value={second_person_plural} class:correct="{second_person_plural_correct}" ></div>
  <div>Ils/Elles <input bind:value={third_person_plural} class:correct="{third_person_plural_correct}" ></div>
</div>

<style>
	.correct {
		background-color: green;
	}
</style>

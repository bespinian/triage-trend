<script lang="ts">
	import type { Prediction } from '../lib/Prediction';
	import { employees } from '$lib/Employee';

	const startDate: string = (new Date()).toISOString().split('T')[0];
	const predictionMap: Map<string, Prediction> = new Map<string, Prediction>();

	interface RequestPayload {
    date: string;
  }
	

  // Function to send the POST request
  async function postData(date: string): Promise<void> {
    const payload: RequestPayload = {
      date: date,
    };

    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data: Prediction = await response.json();
      predictionMap.set(date, data);  // Update the state with the response data
    } catch (err) {
    	err instanceof Error ? err.message : 'Unknown error';
    }
  }

	let isLoaded = false;
	async function loadData() {
	  let i = 0;
		for (; i < 8; i++) {
			await postData(offsetDate(startDate, i));
		}
		isLoaded = true;
	}
    
	function roundedPrediction(date: string): number {
		let prediction = predictionMap.get(date);
		if (prediction) {
			return Math.ceil(prediction.prediction);
		} else {
			return 0;
		}
	}

	function predictionColor(prediction: number): string {
		if (prediction >= 15) {
			return 'bg-error';
		} else if (prediction < 15 && prediction >= 7) {
			return 'bg-warning';
		} else {
			return 'bg-neutral-content';
		}
	}

	function dateText(date: string): string {
		let dateObj = new Date(date);
		const swissGermanDateText = dateObj.toLocaleDateString('de-CH', {
			weekday: 'long',
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
		return swissGermanDateText;
	}

	function offsetDate(date: string, offset: number): string {
		const dateObj = new Date(date);

		dateObj.setDate(dateObj.getDate() + offset);

		return dateObj.toISOString().split('T')[0];
	}

	function getRandomEmployees(count: number): Employee[] {
		const shuffled = employees.sort(() => 0.5 - Math.random());
		return shuffled.slice(0, count);
	}

	loadData();
</script>

{#if isLoaded}
<img src="./clienia-logo.svg" class="m-10 w-56" alt="The logo" />
<div class="h-full mx-auto">
	<div class="w-full min-h-[45vh] mb-7 bg-stone-200">
		<div class="flex flex-row justify-between" data-name="container">
			<div class="bg-amber-200 grow" data-name="left">
				hoi
			</div>
			<div class="bg-emerald-500 grow flex flex-col content-between" data-name="right">
				<div class="bg-cyan-400 flex flex-row justify-start" data-name="prediction">
					<div class="flex flex-col justify-start bg-purple-400" data-name="prediction-date">
						<div class="text-center text-xl font-bold"
							>{dateText(startDate).split(',')[0]}</div
						>
						<div class="text-center text-m"
							>{dateText(startDate).split(',')[1]}</div
						>
					</div>
					<div data-name="prediction-value">
						<div class="text-xl font-bold">
							{roundedPrediction(startDate)} 
						</div>
						<div class="text-m">
							Personen werden heute erwartet
						</div>
					</div>
				</div>
				<div class="bg-fuchsia-400 bg-cyan-400 flex flex-col content-between" data-name="team">
					<div class="" data-name="team-title">
						Einteilung
					</div>
					<div class="" data-name="team-cards">
						cards
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="container mx-auto grid grid-cols-7 gap-2">
		{#each { length: 7 } as _, i}
			<div class="card {predictionColor(roundedPrediction(offsetDate(startDate, i + 1)))}">
				<div class="card-body">
					<span class="text-center text-xl font-bold"
						>{dateText(offsetDate(startDate, i + 1)).split(',')[0]}</span
					>
					<span class="text-center text-m"
						>{dateText(offsetDate(startDate, i + 1)).split(',')[1]}</span
					>
					<p class="text-6xl align-middle text-center">
						{roundedPrediction(offsetDate(startDate, i + 1))}
					</p>
				</div>
			</div>
		{/each}
	</div>
</div>
{/if}

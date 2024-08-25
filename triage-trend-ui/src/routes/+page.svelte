<script lang="ts">
	import type { Prediction } from '$lib/Prediction';
	import type { Employee } from '$lib/Employee';
	import { employees } from '$lib/Employee';
	import MoonNew from '~icons/emojione-v1/new-moon';
  import MoonWaxingCrescent from '~icons/emojione-v1/waxing-crescent-moon';
  import MoonFirstQuarter from '~icons/emojione-v1/first-quarter-moon';
  import MoonWaxingGibbous from '~icons/emojione-v1/waxing-gibbous-moon';
  import MoonFull from '~icons/emojione-v1/full-moon';
  import MoonWaningGibbous from '~icons/emojione-v1/waning-gibbous-moon';
  import MoonLastQuarter from '~icons/emojione-v1/last-quarter-moon';
  import MoonWaningCrescent from '~icons/emojione-v1/waning-crescent-moon';

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

	function teamSize(prediction: number): number {
		if (prediction >= 15) {
			return 5;
		} else if (prediction < 15 && prediction >= 7) {
			return 3;
		} else {
			return 2;
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

	function publicHolidayCantons(date: string): string[] {
		const prediction = predictionMap.get(date);
		let cantons : string[] = [];
		if (prediction?.featuresUsed.publicHolidayZurich === 1) {
			cantons.push('ZH');
		}
		if (prediction?.featuresUsed.publicHolidayAargau === 1) {
			cantons.push('AG');
		}
		if (prediction?.featuresUsed.publicHolidayZug === 1) {
			cantons.push('ZG');
		}
		if (prediction?.featuresUsed.publicHolidaySchaffhausen === 1) {
			cantons.push('SH');
		}
		if (prediction?.featuresUsed.publicHolidaySchwyz === 1) {
			cantons.push('SZ');
		}
		if (prediction?.featuresUsed.publicHolidayStGallen === 1) {
			cantons.push('SG');
		}
		if (prediction?.featuresUsed.publicHolidayThurgau === 1) {
			cantons.push('TG');
		}
		return cantons;
	}

	function getMoonIcon(phase) {
		console.log(phase);
    if (phase === 0) return MoonNew;
    if (phase > 0 && phase <= 12.5) return MoonWaxingCrescent;
    if (phase > 12.5 && phase <= 25) return MoonFirstQuarter;
    if (phase > 25 && phase <= 37.5) return MoonWaxingGibbous;
    if (phase > 37.5 && phase <= 50) return MoonFull;
    if (phase > 50 && phase <= 62.5) return MoonWaningGibbous;
    if (phase > 62.5 && phase <= 75) return MoonLastQuarter;
    if (phase > 75 && phase <= 87.5) return MoonWaningCrescent;
    return MoonNew;
  }

  function openModal(index) {
    const modal = document.getElementById(`modal-${index}`);
    if (modal) {
      modal.showModal();
    }
  }

  function closeModal(index) {
    const modal = document.getElementById(`modal-${index}`);
    if (modal) {
      modal.close();
    }
  }

	loadData();
</script>

{#if isLoaded}
<img src="./clienia-logo.svg" class="m-10 w-56" alt="The logo" />
<div class="h-full mx-auto">
	<div class="w-full min-h-[45vh] mb-7 bg-stone-200">
		<div class="flex flex-row justify-between" data-name="container">
			<div class="grow p-5 min-h-[45vh]" data-name="left">
				<div class="overflow-x-auto mx-10">
				  <table class="table table-sm">
				    <!-- head -->
				    <thead>
				      <tr>
				        <th>Feature</th>
				        <th>Wert</th>
				      </tr>
				    </thead>
				    <tbody>
				      <tr>
				        <td>Kantone mit Feiertag</td>
				        <td>{#each publicHolidayCantons(startDate) as canton}<span>{canton}</span>{/each}</td>
				      </tr>
				      <tr>
				        <td>Regendauer</td>
				        <td>{predictionMap.get(startDate)?.featuresUsed.totalRainDuration} Min.</td>
				      </tr>
				      <tr>
				        <td>Temperatur (&#8960; 5 Tage)</td>
				        <td>{predictionMap.get(startDate)?.featuresUsed.averageTemperature5dayMean} &deg;C</td>
				      </tr>
				      <tr>
				        <td>Luftdruck</td>
				        <td>{predictionMap.get(startDate)?.featuresUsed.averagePressure} hPa</td>
				      </tr>
				      <tr>
				        <td>Luftdruck (&#8960; 5 Tage)</td>
				        <td>{predictionMap.get(startDate)?.featuresUsed.averagePressure5dayMean} hPa</td>
				      </tr>
				      <tr>
				        <td>Temperatur</td>
				        <td>{predictionMap.get(startDate)?.featuresUsed.averageTemperature} &deg;C</td>
				      </tr>
				      <tr>
				        <td>Mondphase</td>
								<td>
									{#if predictionMap.get(startDate)?.featuresUsed?.moonPhase !== undefined}
										{#if getMoonIcon(predictionMap.get(startDate)?.featuresUsed?.moonPhase)}
											<svelte:component
												this={getMoonIcon(predictionMap.get(startDate)?.featuresUsed?.moonPhase)}
												width="30"
												height="30" />
										{:else}
											<span>No data</span>
										{/if}
									{:else}
										<span>No data</span>
									{/if}
								</td>
				    </tbody>
				  </table>
				</div>
			</div>
			<div class="grow flex flex-col content-between p-5 pl-10 {predictionColor(roundedPrediction(startDate))}" data-name="right">
				<div class="flex flex-row justify-start gap-4" data-name="prediction">
					<div class="flex flex-col justify-start" data-name="prediction-date">
						<div class="text-xl font-bold"
							>{dateText(startDate).split(',')[0]}</div
						>
						<div class="text-m"
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
				<div class="divider w-96"></div>
				<div class="flex flex-col content-between" data-name="team">
					<div class="mb-5" data-name="team-title">
						<h1 class="font-bold text-xl">Triageteam</h1>
					</div>
					<div class="flex flex-row justify-start gap-4" data-name="team-cards">
						{#each getRandomEmployees(teamSize(roundedPrediction(startDate))) as employee}
							<div class="card bg-base-100 w-32 shadow-xl">
								<figure class="h-32">
							    <img
							    	class="object-cover h-full w-full"
							      src="{employee.imagePath}"
							      alt="{employee.name}" />
							  </figure>
							  <div class="card-body px-5 py-2">
							    <p>{employee.firstName} {employee.lastName}</p>
							  </div>
							</div>
						{/each}
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="container mx-auto grid grid-cols-7 gap-2">

		{#each { length: 7 } as _, i}
			<div 
				class="card {predictionColor(roundedPrediction(offsetDate(startDate, i + 1)))}" 
				on:click={() => openModal(i)}
			>
				<div class="card-body">
					<span class="text-center text-xl font-bold">
						{dateText(offsetDate(startDate, i + 1)).split(',')[0]}
					</span>
					<span class="text-center text-m">
						{dateText(offsetDate(startDate, i + 1)).split(',')[1]}
					</span>
					<p class="text-6xl align-middle text-center">
						{roundedPrediction(offsetDate(startDate, i + 1))}
					</p>
				</div>
			</div>
			<!-- Modal for each card -->
			<dialog id={`modal-${i}`} class="modal">
				<div class="modal-box w-11/12 max-w-5xl">
					<div class="flex flex-row justify-between" data-name="container">
						<div class="grow p-5" data-name="left">
							<div class="overflow-x-auto mx-10">
								<table class="table table-sm">
									<thead>
										<tr>
											<th>Feature</th>
											<th>Wert</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>Kantone mit Feiertag</td>
											<td>
												{#each publicHolidayCantons(offsetDate(startDate, i + 1)) as canton}
													<span>{canton}</span>
												{/each}
											</td>
										</tr>
										<tr>
											<td>Regendauer</td>
											<td>{predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed.totalRainDuration} Min.</td>
										</tr>
										<tr>
											<td>Temperatur (&#8960; 5 Tage)</td>
											<td>{predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed.averageTemperature5dayMean} &deg;C</td>
										</tr>
										<tr>
											<td>Luftdruck</td>
											<td>{predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed.averagePressure} hPa</td>
										</tr>
										<tr>
											<td>Luftdruck (&#8960; 5 Tage)</td>
											<td>{predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed.averagePressure5dayMean} hPa</td>
										</tr>
										<tr>
											<td>Temperatur</td>
											<td>{predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed.averageTemperature} &deg;C</td>
										</tr>
										<tr>
											<td>Mondphase</td>
											<td>
												{#if predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed?.moonPhase !== undefined}
													{#if getMoonIcon(predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed?.moonPhase)}
														<svelte:component
															this={getMoonIcon(predictionMap.get(offsetDate(startDate, i + 1))?.featuresUsed?.moonPhase)}
															width="30"
															height="30" />
													{:else}
														<span>No data</span>
													{/if}
												{:else}
													<span>No data</span>
												{/if}
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
						<div class="grow flex flex-col rounded-lg content-between p-5 pl-10 {predictionColor(roundedPrediction(offsetDate(startDate, i + 1)))}" data-name="right">
							<div class="flex flex-row justify-start gap-4" data-name="prediction">
								<div class="flex flex-col justify-start" data-name="prediction-date">
									<div class="text-xl font-bold">
										{dateText(offsetDate(startDate, i + 1)).split(',')[0]}
									</div>
									<div class="text-m">
										{dateText(offsetDate(startDate, i + 1)).split(',')[1]}
									</div>
								</div>
								<div data-name="prediction-value">
									<div class="text-xl font-bold">
										{roundedPrediction(offsetDate(startDate, i + 1))} 
									</div>
									<div class="text-m">
										Personen werden heute erwartet
									</div>
								</div>
							</div>
							<div class="divider w-96"></div>
							<div class="flex flex-col content-between" data-name="team">
								<div class="mb-5" data-name="team-title">
									<h1 class="font-bold text-xl">Triageteam</h1>
								</div>
								<div class="flex flex-row justify-start gap-4" data-name="team-cards">
									{#each getRandomEmployees(teamSize(roundedPrediction(offsetDate(startDate, i + 1)))) as employee}
										<div class="card bg-base-100 w-32 shadow-xl">
											<figure class="h-32">
												<img
													class="object-cover h-full w-full"
													src="{employee.imagePath}"
													alt="{employee.name}" />
											</figure>
											<div class="card-body px-5 py-2">
												<p>{employee.firstName} {employee.lastName}</p>
											</div>
										</div>
									{/each}
								</div>
							</div>
						</div>
					</div>
					<div class="modal-action">
						<button class="btn" on:click={() => closeModal(i)}>Close</button>
					</div>
				</div>
			</dialog>
		{/each}

	</div>
</div>
{/if}

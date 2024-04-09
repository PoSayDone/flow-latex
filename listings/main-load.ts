export const load: LayoutServerLoad = async ({ fetch }) => {
	const profile: UserWStatus = await (await fetch('http://nginx/api/user/profile')).json();
	const trip_purposes: TripPurpose[] = await (await fetch('http://nginx/api/trip_purposes')).json();
	const interests: Interest[] = await (await fetch('http://nginx/api/interests')).json();
	const departures: Departure[] = await (await fetch('http://nginx/api/departures')).json();
	const arrivals: Arrival[] = await (await fetch('http://nginx/api/arrivals')).json();

    // ...

	const data = {
		user: profile,
		interests: interests,
		trip_purposes: trip_purposes,
		departures: departures,
		arrivals: arrivals,
		statusForm,
		profileForm,
		interestsForm,
		likeForm,
		avatarForm
	};

	return data;
};

export const actions = {
  update_interests: async ({ request, fetch }) => {
    const interestsForm = await superValidate(request, zod(interestsSchema));
    if (!interestsForm.valid) return fail(400, { interestsForm });
    await fetch("http://nginx/api/user/interests/edit", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        tags: interestsForm.data.user_interests,
      }),
    });
  },
  update_status: async ({ request, fetch }) => {
    const statusForm = await superValidate(request, zod(statusSchema));
    if (!statusForm.valid) return fail(400, { statusForm });
    await fetch("http://nginx/api/user/status_data/edit", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(statusForm.data),
    });
  },
  update_profile: async ({ request, fetch }) => {
    const profileForm = await superValidate(request, zod(profileSchema));
    if (!profileForm.valid) return fail(400, { profileForm });
    await fetch("http://nginx/api/user/", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(profileForm.data),
    });
  },
  update_avatar: async ({ request, fetch }) => {
    const formData = await request.formData();
    const avatarForm = await superValidate(
      { file: formData.get("file") as File },
      zod(avatarSchema),
    );
    if (!avatarForm.valid) {
      return fail(400, { avatarForm });
    }
    await fetch("http://nginx/api/user/image", {
      method: "PATCH",
      body: formData,
    });
  },
} satisfies Actions;

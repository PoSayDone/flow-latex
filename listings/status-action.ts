export const actions = {
  //...
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
  //...
} satisfies Actions;

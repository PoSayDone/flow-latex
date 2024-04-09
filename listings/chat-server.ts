export const actions = {
  send_message: async ({ request, fetch, params }) => {
    const messageForm = await superValidate(request, zod(messageSchema));
    if (!messageForm.valid) return fail(400, { messageForm });
    await fetch(`http://nginx/api/chats/${params.conversation_id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        content: messageForm.data.message,
      }),
    });
  },
} satisfies Actions;

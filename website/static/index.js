function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId:noteId }),
    }).then((_res) => {
      window.location.href = "/";
    })
    console.log('note id' + noteId);
};

function updateNote(noteId,note){
  fetch("/update-note",{
    method:"POST",
    body: JSON.stringify({noteId:noteId,note:note})
  }).then((_res) => {
    window.location.href = "/";
  });
};

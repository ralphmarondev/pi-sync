namespace PiSync.Room.NewRoom
{
    partial class NewRoomForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnSave = new Button();
            btnCancel = new Button();
            label1 = new Label();
            tbRoomName = new TextBox();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Controls.Add(btnSave);
            panel1.Controls.Add(btnCancel);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(tbRoomName);
            panel1.Location = new Point(12, 12);
            panel1.Name = "panel1";
            panel1.Size = new Size(343, 226);
            panel1.TabIndex = 0;
            // 
            // btnSave
            // 
            btnSave.Cursor = Cursors.Hand;
            btnSave.Location = new Point(182, 134);
            btnSave.Name = "btnSave";
            btnSave.Size = new Size(133, 47);
            btnSave.TabIndex = 5;
            btnSave.Text = "SAVE";
            btnSave.UseVisualStyleBackColor = true;
            btnSave.Click += btnSave_Click;
            // 
            // btnCancel
            // 
            btnCancel.Cursor = Cursors.Hand;
            btnCancel.Location = new Point(26, 134);
            btnCancel.Name = "btnCancel";
            btnCancel.Size = new Size(133, 47);
            btnCancel.TabIndex = 4;
            btnCancel.Text = "CANCEL";
            btnCancel.UseVisualStyleBackColor = true;
            btnCancel.Click += btnCancel_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(26, 37);
            label1.Name = "label1";
            label1.Size = new Size(120, 21);
            label1.TabIndex = 3;
            label1.Text = "Room Name:";
            // 
            // tbRoomName
            // 
            tbRoomName.Location = new Point(26, 64);
            tbRoomName.Name = "tbRoomName";
            tbRoomName.PlaceholderText = "Enter room name";
            tbRoomName.Size = new Size(289, 30);
            tbRoomName.TabIndex = 2;
            tbRoomName.TextAlign = HorizontalAlignment.Center;
            // 
            // NewRoomForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(370, 257);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 3, 4, 3);
            Name = "NewRoomForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "NEW ROOM";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label label1;
        private TextBox tbRoomName;
        private Button btnSave;
        private Button btnCancel;
    }
}